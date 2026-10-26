# login_decision.py
# This program will make a decision based on login credentials and failed attempt counts.
MAX_FAILED = 5
KNOWN_USERS = "analyst"
STORED_PASSWORDS = "Blue#Falcon72"

username = input("Username: ")
failed = int(input("Failed attempts so far: "))
password = input("Password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USERS:
    print("Unknown user.")
elif password != STORED_PASSWORDS:
    attempts_left = MAX_FAILED - failed - 1
    print(f"Access denied. Attempts left:")
else:
    print("Access granted.")   