# port_report.py
# This program will ask the user for a start and end port number, and then it will print out the port number along with its type (system, user, or dynamic). It will also keep track of how many ports have been checked.
start_port = int(input("Start port: " ))
end_port = int(input("End port: " ))

ports_checked = 0
for port in range(start_port, end_port + 1):
    if port <= 1023:
        port_type = "system"
    elif port <= 49151:
        port_type = "user"
    else:
        port_type = "dynamic"
    print(f"{port}: {port_type}")
    
    ports_checked += 1

    print("Ports checked: ", ports_checked)