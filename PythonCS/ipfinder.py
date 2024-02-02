import socket
import requests
import subprocess

def get_local_ip():
    try:
        # Get the hostname of the local machine
        host_name = socket.gethostname()        
        # Get the IP address corresponding to the hostname
        ip_address = socket.gethostbyname(host_name)
        print(f"IP Address of {host_name}: {ip_address}")
    except socket.error as e:
        print(f"Error: {e}")



def get_public_ip():
    try:
        # Use an external service to get the public IP address
        response = requests.get('https://api64.ipify.org?format=json')
        ip_data = response.json()
        public_ip = ip_data['ip']
        print(f"Your public IP address is: {public_ip}")
    except requests.RequestException as e:
        print(f"Error: {e}")


def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Attempt to connect to the target's port
        result = sock.connect_ex((target, port))

        # If the connection is successful, the port is open
        if result == 0:
            open_ports.append(port)
            print(port)

        # Close the socket
        sock.close()

    return open_ports


def find_open_port_in_range():
    target_host = input("Enter the target host (e.g., 'localhost' or an IP address): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open.")
    else:
        print("No open ports found.")

    


def get_open_ports():
    try:
        # Run the netstat command and capture the output
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)

        # Split the output into lines and filter for lines containing "LISTENING"
        listening_lines = [line for line in result.stdout.split('\n') if 'LISTENING' in line]

        # Extract the local address and port from each listening line
        open_ports = [line.split()[1] for line in listening_lines]

        return open_ports
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def find_open_port_by_command():
    open_ports = get_open_ports()

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("Error retrieving open ports.")


def get_connected_ips_and_ports():
    try:
        # Run the netstat command and capture the output
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)

        # Split the output into lines and filter for lines containing "ESTABLISHED"
        established_lines = [line for line in result.stdout.split('\n') if 'ESTABLISHED' in line]

        # Extract the remote address and port from each established connection
        connected_ips_and_ports = [(line.split()[1], line.split()[2].split(':')[1]) for line in established_lines]

        return connected_ips_and_ports
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def get_connected_ips_and_ports_by_command():
    connected_ips_and_ports = get_connected_ips_and_ports()

    if connected_ips_and_ports:
        print("Connected IPs and Ports:")
        for ip, port in connected_ips_and_ports:
            print(f"IP: {ip}, Port: {port}")
    else:
        print("Error retrieving connected IPs and Ports.")



if __name__ == "__main__":
    get_local_ip()
    get_public_ip()
    find_open_port_by_command()
    get_connected_ips_and_ports_by_command()
