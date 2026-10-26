#device_card.py
#this program stores and displays network device information
#consent
MAX_CONNECTIONS = 80
#variables
device_name = "web_server_02"
device_ip = "192.168.1.103"
service = "http"
open_ports = 412
#print each vallue with a label
print("Device:", device_name)
print("Ip address:", device_ip)
print("Service:", service)
print("Port:", open_ports)
print("Max connections:", MAX_CONNECTIONS)
#change two values
service = "ssh"
open_ports = 22
#print new values in one line
print("updated service:", service, "on port:", open_ports)