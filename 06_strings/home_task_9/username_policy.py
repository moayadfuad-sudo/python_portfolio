# username_policy.py
# this program checks if a username is valid according to the following rules:
# 1. The username must be between 3 and 12 characters long.
# 2. The username must start with a letter.
# 3. The username can only contain letters, numbers, and underscores.

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return the username without surrounding whitespace, in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first character that is not a letter, digit, or underscore."""
    for character in username:
        if not (character.isalpha() or character.isdecimal() or character == "_"):
            return character
    return ""


def policy_problem(username):
    """Return the first username policy problem, or an empty string."""
    if not MIN_LENGTH <= len(username) <= MAX_LENGTH:
        return f"length must be {MIN_LENGTH} to {MAX_LENGTH}."

    if not username[0].isalpha():
        return "it must start with a letter."

    character = bad_character(username)
    if character:
        return f"the character {character} is not allowed."

    return ""


username = clean(input("New username: "))
problem = policy_problem(username)

if problem:
    print(f"Rejected [{username}]: {problem}")
else:
    print(f"Accepted [{username}].")