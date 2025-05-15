#Problem: Create a program that validates a user's email address. The email must:

# Contain "@" and "."
# Have text before "@" and after the last "."


import re
def validate_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

print(validate_email("test@example.com"))

print(validate_email("inavlid.com"))
print(validate_email("invalid@com"))
