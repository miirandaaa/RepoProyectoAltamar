from datetime import datetime
from src.exceptions import InvalidInputException

def validate_input(value, type, value_func=None, allow_none=False, error_message=None):
    if value is None and allow_none:
        return True
    if not isinstance(value, type):
        raise InvalidInputException(error_message if error_message is not None else f"Invalid input. Expected {type}.")
    
    if value_func is not None:
        return value_func(value, error_message=error_message)
    
    return True


def validate_list_of_type(lst, expected_type, error_message="Invalid input. Expected list"):
    if not isinstance(lst, list):
        raise InvalidInputException(error_message)
    for item in lst:
        if not isinstance(item, expected_type):
            raise InvalidInputException(f"Invalid input. Expected list of {expected_type}.")
    return True


def validate_date(date, error_message="Invalid date format. Expected dd-mm-yyyy."):
    try:
        datetime.datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        raise InvalidInputException(error_message)
    

def validate_email(email, error_message="Invalid email format."):
    # Regex for email validation
    import re
    regex = r'^\S+@\S+\.\S+$'
    if re.search(regex, email):
        return True
    raise InvalidInputException(error_message)


def convert_to_standard_date(date_string):
    # Lista de posibles formatos de entrada
    date_formats = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%m-%d-%Y", "%m/%d/%Y"]
    
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_string, date_format)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    raise ValueError("Invalid date format. Please use a valid date format (e.g., 2020-07-05 or 05/07/2020).")