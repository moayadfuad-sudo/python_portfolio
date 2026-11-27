# fix_the_parser.py

LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: the time long is always 5 characters, so we can use slicing to extract it.
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]

    # semantic: it backwards to convert the username to lowercase after extracting it from the line. 
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: the comparison is case-sensitive; convert the line to lowercase.
    return "failed" in line.lower()


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings are immutable in Python; create a new string.
    return "*" + user[1:]


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")

# runtime: the length is An independent function, not a method of the text.
print(f"Length: {len(LINE)}")