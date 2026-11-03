# pin_tries.py
# this program allows the user to enter a PIN and has a limited number of attempts
MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0

while tries < MAX_TRIES:
    pin = input("PIN: ")
    tries += 1

    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    print("Wrong PIN. tries left:", MAX_TRIES - tries)
else:
    print("card blocked.")