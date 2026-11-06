# password_check.py
#  This module provides functions to check if a password meets certain criteria, such as length and difference from the username.
def long_enough(password, minimum=8):
    """Check if the password is long enough."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Check if password is different from username."""
    return password != username


def password_ok(password, username):
    """Check if the password meets all requirements."""
    return long_enough(password) and differs_from_username(password, username)


username = input("Enter username: ")
password = input("Enter password: ")

if password_ok(password, username):
    print("Password accepted")
else:
    print("Password rejected")