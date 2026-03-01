class APIException(Exception):
    def __init__(self, message, status_code=500, details=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

class ValidationError(APIException):
    def __init__(self, message, details=None):
        super().__init__(message, 400, details)

class AuthenticationError(APIException):
    def __init__(self, message="Authentication required", details=None):
        super().__init__(message, 401, details)

class AuthorizationError(APIException):
    def __init__(self, message="Access denied", details=None):
        super().__init__(message, 403, details)

class NotFoundError(APIException):
    def __init__(self, message="Resource not found", details=None):
        super().__init__(message, 404, details)

class ConflictError(APIException):
    def __init__(self, message="Resource conflict", details=None):
        super().__init__(message, 409, details)

class InternalServerError(APIException):
    def __init__(self, message="Internal server error", details=None):
        super().__init__(message, 500, details)
