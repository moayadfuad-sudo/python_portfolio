#ip_check.py
# this program checks if an IPv4 address is valid. It returns the first problem found, or an empty string if the address is valid.
def is_valid_part(part):
    """Return True if part contains only digits and its value is at most 255."""
    return part.isdecimal() and int(part) <= 255


def ip_problem(address):
    """Return the first problem found in an IPv4 address, or an empty string."""
    if address.count(".") != 3:
        return "it needs exactly 3 dots."

    for part in address.split("."):
        if part == "":
            return "a part is empty."
        if not is_valid_part(part):
            return f"{part} is not a number from 0 to 255."

    return ""


address = input("IPv4 address: ").strip()
problem = ip_problem(address)

if problem:
    print(f"Invalid: {problem}")
else:
    print(f"{address} is valid.")