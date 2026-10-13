#port_facts.py
# References: RFC 9293 (TCP) and RFC 791 (IPv4)

# 1. Store bit lengths in constants
TCP_PORT_BITS = 16
IPV4_BITS = 32

# 2. Calculate network metrics using exponentiation (**)
total_ports = 2 ** TCP_PORT_BITS
highest_port = (2 ** TCP_PORT_BITS) - 1
total_ipv4_addresses = 2 ** IPV4_BITS

# 3. Print each result with an f-string
print(f"Total possible TCP ports: {total_ports}")
print(f"Highest port number: {highest_port}")
print(f"Total possible IPv4 addresses: {total_ipv4_addresses}")