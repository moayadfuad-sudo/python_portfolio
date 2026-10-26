#port_classifier.py
# this program will classify the port number into system, user, or dynamic/private range and also identify some common services
port = int(input("port: "))

if port < 0 or port > 65535:
    print("invalid port : use a number from 0 to 65535")

else:
    if 0 <= port <= 1023:
      if port == 22:
        print("Range: system\nservices: ssh")
      elif port == 80:
        print("Range: system\nservices: http")
      else:
        print("Range: system")
    elif 1024 <= port <= 49151:
      if port == 443:
        print("Range: user\nservices: https")
      else:
       print("Range: user")
    else:
        print("Range: dynamic or private")