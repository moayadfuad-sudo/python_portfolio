# lock_tools.py
# This module provides functions to check if an account is locked, how many tries are left, and the account status based on the number of failed login attempts.
def is_locked(failed, max_tries=3):
    """Check if the account is locked."""
    return failed >= max_tries


def tries_left(failed, max_tries=3):
    """Calculate how many tries are left."""
    return max(0, max_tries - failed)


def status(failed):
    """Return the account status."""
    if is_locked(failed):
        return "locked"
    return f"active ({tries_left(failed)} tries left)"


print(is_locked(2))
print(is_locked(3))
print(is_locked(1))
print(tries_left(1))
print(tries_left(3))
print(status(1))
print(status(3))