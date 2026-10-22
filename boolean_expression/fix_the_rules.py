# fix_the_rules.py
# This program checks a connection against three rules .
role = input("Role: ")
#Runtime error: convert the input to int before comparing
port = int(input("Port: "))
#semantic error: use == to compare the role with "admin"
is_admin = role == "admin"
#Runtime error: convert port to int before comparing
is_system_port = port <= 1023
#semantic error: use == to compare the port with 80 or 443
is_web_port = port == 80 or 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")