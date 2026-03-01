import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from jinja2 import Template

logger = logging.getLogger(__name__)


class EmailService:
    def __init__(self, config):
        self.smtp_host = config.SMTP_HOST
        self.smtp_port = config.SMTP_PORT
        self.smtp_user = config.SMTP_USER
        self.smtp_password = config.SMTP_PASSWORD
        self.smtp_from = config.SMTP_FROM_EMAIL
        self.admin_email = config.ADMIN_EMAIL
        self.debug = config.DEBUG
    
    def _load_template(self, template_name):
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'templates',
            template_name
        )
        with open(template_path, 'r') as f:
            return f.read()
    
    def _send_email(self, to_email, subject, html_content):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.smtp_from
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, 'html'))
        
        if self.debug or not self.smtp_user:
            logger.info(f"[MOCK SMTP] Would send email to {to_email}")
            logger.info(f"[MOCK SMTP] Subject: {subject}")
            logger.info(f"[MOCK SMTP] Body preview: {html_content[:200]}...")
            return True
        
        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                if self.smtp_port in [465, 587]:
                    server.starttls()
                if self.smtp_user and self.smtp_password:
                    server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
            logger.info(f"Email sent successfully to {to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            raise
    
    def send_contact_notification(self, name, email, subject, message):
        template = Template(self._load_template('contact_notification.html'))
        html_content = template.render(
            name=name,
            email=email,
            subject=subject,
            message=message,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        return self._send_email(self.admin_email, f"New Contact: {subject}", html_content)
    
    def send_confirmation(self, name, email):
        template = Template(self._load_template('contact_confirmation.html'))
        html_content = template.render(
            name=name,
            confirmation_message="Thank you for your message. We will get back to you soon!"
        )
        return self._send_email(email, "Thank you for contacting us", html_content)
