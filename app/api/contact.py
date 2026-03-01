from flask import request
from flask_restx import Namespace, Resource, fields
from pydantic import BaseModel, EmailStr, ValidationError
from app import email_service
import logging

logger = logging.getLogger(__name__)

api = Namespace('contact', description='Contact form operations')

contact_model = api.model('Contact', {
    'name': fields.String(required=True, description='Full name'),
    'email': fields.String(required=True, description='Email address'),
    'subject': fields.String(required=True, description='Subject'),
    'message': fields.String(required=True, description='Message')
})

class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


@api.route('')
class ContactResource(Resource):
    @api.expect(contact_model)
    @api.response(201, 'Contact form submitted successfully')
    @api.response(400, 'Validation error')
    @api.response(500, 'Internal server error')
    def post(self):
        data = request.get_json()
        
        try:
            validated = ContactRequest(**data)
        except ValidationError as e:
            return {'error': 'Validation failed', 'details': e.errors()}, 400
        
        try:
            email_service.send_contact_notification(
                name=validated.name,
                email=validated.email,
                subject=validated.subject,
                message=validated.message
            )
        except Exception as e:
            logger.error(f"Failed to send notification email: {str(e)}")
            return {'error': 'Failed to send notification email'}, 500
        
        try:
            email_service.send_confirmation(name=validated.name, email=validated.email)
        except Exception as e:
            logger.warning(f"Failed to send confirmation email: {str(e)}")
        
        logger.info(f"Contact form submitted by {validated.email}")
        return {'message': 'Contact form submitted successfully'}, 201
