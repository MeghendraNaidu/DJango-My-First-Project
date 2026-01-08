import re

USERNAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{4,19}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
PASSWORD_REGEX = re.compile(
    r'^(?=(?:.*[A-Z]){2})(?=(?:.*[a-z]){2})(?=(?:.*\d){2})(?=(?:.*[#@$!%*?&]){2})[A-Za-z\d#@$!%*?&]{8,}$'
)

def validate_username(username):
    return bool(USERNAME_REGEX.match(username))

def validate_email(email):
    return bool(EMAIL_REGEX.match(email))

def validate_password(password):
    return bool(PASSWORD_REGEX.match(password))
