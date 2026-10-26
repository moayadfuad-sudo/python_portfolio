#conditional_tests.py
#this program contains ten conditional tests using boolean expressions. 
user = "analyst"
role = "viewer"
failed = 3
port = 22
print("is failed >=3? i predict True")
print(failed >=3)
print("\n is port < 20? i predict False")
print(port < 20)
print("\n is user == 'analyst'? i predict True")
print(user == 'analyst')
print("\n is role != 'viewer'? i predict False")
print(role != 'viewer')
print("\n is failed <= 5? i predict True")
print(failed <= 5)
print("\n is port >2 or port < 30? i predict True")
print(port > 2 or port < 30)
print("\n is user == 'viewer' and role == 'analyst'? i predict False")
print(user == 'viewer' and role == 'analyst')
print("\n is failed == 3 and port == 22? i predict True")
print(failed == 3 and port == 22)
print("\n is user == 'analyst' and port == 22? i predict True")
print(user == 'analyst' and port == 22)
print("\n not failed == 3 or port != 22? i predict False")
print(not failed == 3 or port !=22)