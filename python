import socket
import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

def port_scan(target_ip, port_range):
    print(f'Starting scan on host {target_ip}...\n')

    # Iterate through ports in the specified range
    for port in range(*port_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the target port
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f'Port {port}: Open')
        sock.close()

    print('\nScan finished.')

def main():
    # Generate ASCII art banner with username
    username = "Your Username"  # Replace with your actual username
    ascii_banner = generate_ascii_art(username)
    print(ascii_banner)

    # Input for target IP address and port range
    target_ip = input('Enter the target IP address to scan: ')
    start_port = int(input('Enter the starting port number: '))
    end_port = int(input('Enter the ending port number: ')) + 1  # Add 1 to include the end port

    port_range = (start_port, end_port)
    port_scan(target_ip, port_range)

if __name__ == '__main__':
    main()
