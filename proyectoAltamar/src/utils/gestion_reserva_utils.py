class AddHuespedError(Exception):
    """General exception for user creation errors."""
    pass

class HuespedAlreadyExists (AddHuespedError):
    """Exception for when the user already exists"""
    pass