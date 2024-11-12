import socket

def reverse_dns_lookup(ip_address):
    try:
        # Perform reverse DNS lookup (IP to URL)
        url = socket.gethostbyaddr(ip_address)
        return url[0]  # The first element is the primary domain name
    except socket.herror:
        return f"Could not resolve {ip_address}"

def forward_dns_lookup(url):
    try:
        # Perform forward DNS lookup (URL to IP)
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return f"Could not resolve {url}"

def main():
    choice = input("Choose lookup type:\n1. IP to URL (Reverse DNS)\n2. URL to IP (Forward DNS)\nEnter choice (1/2): ")

    if choice == '1':
        ip_address = input("Enter IP address to lookup: ")
        result = reverse_dns_lookup(ip_address)
        print(f"Reverse DNS lookup result: {result}")
    elif choice == '2':
        url = input("Enter URL to lookup: ")
        result = forward_dns_lookup(url)
        print(f"Forward DNS lookup result: {result}")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
