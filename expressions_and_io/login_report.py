#login_report.py
MAX_LOGIN_ATTEMPTS = 5
username = input("username: ")
failed = int(input("failed attempts: "))
#how many attempts are left
attempts_left = MAX_LOGIN_ATTEMPTS - failed
print("="*30)
print("LOGIN REPORT")
print("="*30)
print(f"User:\t\t{username}")
print(f"Failed:\t\t{failed}")
print(f"attempts left:\t\t{attempts_left}")
print("="*30)