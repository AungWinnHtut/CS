import socket

def check_port(ip, port):
    try:
        # Create a socket object
        sock = socket.create_connection((ip, port), timeout=5)
        sock.close()
        return True  # Port is open
    except (socket.timeout, socket.error):
        return False  # Port is closed

# Example usage
ip_address = "0.tcp.ap.ngrok.io"
port_to_check = 12668

if check_port(ip_address, port_to_check):
    print(f"Port {port_to_check} is open at {ip_address}")
else:
    print(f"Port {port_to_check} is closed at {ip_address}")
