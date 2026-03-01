import re

def validate_email(email):
    return re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email)

def validate_username(username):
    return re.match(r'^[a-zA-Z0-9_]{3,50}$', username)

def validate_password(password):
    return len(password) >= 6

def validate_register(data):
    errors = []
    if not data.get('username') or not validate_username(data['username']):
        errors.append('Username must be 3-50 alphanumeric characters or underscore')
    if not data.get('email') or not validate_email(data['email']):
        errors.append('Invalid email format')
    if not data.get('password') or not validate_password(data['password']):
        errors.append('Password must be at least 6 characters')
    return errors

def validate_login(data):
    errors = []
    if not data.get('email') or not data.get('password'):
        errors.append('Email and password are required')
    return errors
