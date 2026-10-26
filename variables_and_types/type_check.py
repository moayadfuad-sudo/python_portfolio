#type_check.py
#print the type of each value
print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))
#8080=int,"8080"=str,99.5=float,"198.51.100.7"=str,1_000=int
print(int("443"))
print(str(8080))
print(float(2.5))
#print each converted value and its type
print(int("443"), type(int("443")), str(8080), type(str(8080)), float("2.5"),type(float("2.5")))