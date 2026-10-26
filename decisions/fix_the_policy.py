# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12
    
username = input("Username: ")
password = input("New password: ")

 #syntax error: expected ':'   
if len(password) < MIN_LENGTH:
    print("- Too short.")
# semantic error: check whether the password matches the username.
elif password == username:
    print("- Same as the username.")

#Semantic error fix: check for "long" first. Otherwise, passwords of
# 16 or more characters would already match the >= 12 condition below.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
    print(f"Length: {len(password)} ({strength})")
