# security_toolkit.py
# # This program provides a security toolkit to check port ranges, password problems, and PIN guessing time.

MIN_LENGTH = 8


def border(width):
    """Print a border for a box of the given width."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a box."""
    border(len(text))
    print("| " + text + " |")
    border(len(text))


def show_menu():
    """Display the security toolkit menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return the range name for a port."""
    if port < 0 or port > 65535:
        return "invalid"
    elif port <= 1023:
        return "system"
    elif port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Ask for a port and display its range in a box."""
    port = int(input("Port: "))
    result = port_range(port)
    show_box(f"Port {port}: {result}")


def password_problem(password, username):
    """Return the first password problem, or an empty string."""
    if len(password) < MIN_LENGTH:
        return "too short"
    elif password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask for a username and password, then display the result."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Return whole days to try every PIN combination."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask for PIN digits and speed, then display the time estimate."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


show_menu()
checks_done = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks_done += 1
    elif choice == "2":
        check_password()
        checks_done += 1
    elif choice == "3":
        check_pin()
        checks_done += 1
    elif choice == "q":
        break
    else:
        print("Unknown choice.")

show_box(f"Checks done: {checks_done}")
