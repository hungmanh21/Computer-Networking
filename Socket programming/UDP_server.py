import socket

serverName = socket.gethostname()
IP = socket.gethostbyname(serverName)
print(IP)
# port number like UDP client
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

'''
The below line binds (that is, assigns) the port number 12000 to the server’s socket.
Thus, in UDPServer, the code (written by the application developer) is explicitly
assigning a port number to the socket. In this manner, when anyone sends a packet to
port 12000 at the IP address of the server, that packet will be directed to this socket.
UDPServer then enters a while loop; the while loop will allow UDPServer to receive
and process packets from clients indefinitely. In the while loop, UDPServer waits for
a packet to arrive.
'''
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Received data from {clientAddress}: {message.decode()}")
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)