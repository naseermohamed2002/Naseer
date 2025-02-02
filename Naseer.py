import socket
import pyfiglet


def generate_ascii_art(name):
    ascii_art = pyfiglet.figlet_format(name)
    return ascii_art

def port_scan(target_host, port_range):
    try:
        # Resolve IP address of the target host
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"Couldn't resolve hostname '{target_host}'")
        return

    # Your name for ASCII art
    your_name = "Naseer"  # Replace with your actual name
    ascii_name = generate_ascii_art(your_name)
    print(ascii_name)

    print(f'Starting scan on host {target_ip} ({target_host})...\n')

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

if __name__ == '__main__':
    target_host = input('Enter the target host to scan: ')
    start_port = int(input('Enter the starting port number: '))
    end_port = int(input('Enter the ending port number: ')) + 1  # Add 1 to include the end port

    port_range = (start_port, end_port)
    port_scan(target_host, port_range)
