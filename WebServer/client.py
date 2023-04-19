import sys
import socket


def http_client(server_host, server_port, filename):
    # Open a TCP connection to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Send an HTTP GET request to the server
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}:{server_port}\r\n\r\n"
    client_socket.send(request.encode())

    # Receive the server response and display it
    response = b''
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data
    print(response.decode())

    # Close the TCP connection
    client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: client.py server_host server_port filename')
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    http_client(server_host, server_port, filename)
