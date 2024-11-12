import ipaddress

def get_ip_details(ip_addr, subnet_mask):
    # Calculate network and broadcast addresses
    network = ipaddress.IPv4Network(f"{ip_addr}/{subnet_mask}", strict=False)
    
    # Determine IP class
    first_octet = int(ip_addr.split('.')[0])
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    elif 224 <= first_octet <= 239:
        ip_class = 'D (Multicast)'
    else:
        ip_class = 'E (Experimental)'
    
    # Display IP address details
    print(f"IP Address: {ip_addr}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Class: {ip_class}")
    print(f"Network Address: {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"First Usable IP Address: {list(network.hosts())[0]}")
    print(f"Last Usable IP Address: {list(network.hosts())[-1]}")
    print(f"Total Number of Usable Hosts: {network.num_addresses - 2}")

# Get user input
ip_addr = input("Enter IP Address (e.g., 192.168.1.1): ")
subnet_mask = input("Enter Subnet Mask (e.g., 255.255.255.0): ")

# Display IP details
get_ip_details(ip_addr, subnet_mask)
