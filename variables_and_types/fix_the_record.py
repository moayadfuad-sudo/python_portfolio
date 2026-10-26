#fix_the_record.py
#this program prints a short record about a network device
device_name = "edge-router"
#syntax error: variable name cannot start with a number
second_ip = "192.0.2.1"
#syntax error: "class" is a reserved word in python
class_section = "router"
#Runtime error: cannot convert string to int
port = int("22")
#Runtime error: printed "device_nam" which is not defined
print("device:", device_name)
#syntax error: variable name cannot start with a number
print("Backup ip:", second_ip)
#syntax error: "class" is a reserved word in python
print("Type:", class_section)
#runtime error: cannot convert string to int
print("Port:", port) 
#python reports syntax errors first (like invalid variable names or reserved keywords)
# during the parsing phase before running the code. Runtime errors (like ValueError)
# are only detected later when the code actually executes