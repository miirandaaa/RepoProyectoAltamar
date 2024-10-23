class BusinessLogicException(Exception):
    status_code = 500

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ResourceNotFoundException(BusinessLogicException):
    status_code = 404

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidInputException(BusinessLogicException):
    status_code = 400

    def __init__(self, message):
        super().__init__(message)
        self.message = message

class UnauthorizedException(BusinessLogicException):
    status_code = 401

    def __init__(self, message):
        super().__init__(message)
        self.message = message