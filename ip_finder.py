import socket

def get_ip_address(domain_name):
    try:
        # Get the IP address
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Unable to resolve domain name"

# Example usage
domain = "www.amazon.com"
ip = get_ip_address(domain)
print(f"The IP address of {domain} is: {ip}")