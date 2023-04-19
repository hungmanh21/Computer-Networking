# import library
import socket

# serverName : IP address (e.g., “128.138.32.126”) or the host name (e.g., “cis.poly.edu”)
serverName = socket.gethostname()
# set the port number
serverPort = 12000

'''
create client's socket
first parameter indicates the address family. In this case AF_INET indicates that the underlying network is using IPv4
The second parameter indicates that the socket is of type SOCK_DGRAM, which means it is a UDP socket
'''
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input lowercase sentence:')

'''
Convert message from string type to byte type
The method sendto() attaches the destination address (serverName, serverPort) 
to the message and sends the resulting packet into the process’s socket, clientSocket.
'''
clientSocket.sendto(message.encode(), (serverName, serverPort))

'''
When a packet arrives from the Internet at the client’s socket, the 
packet’s data is put into the variable modifiedMessage and the packet’s source
address is put into the variable serverAddress
The variable serverAddress contains both the server’s IP address and the server’s port number
The method recvfrom also takes the buffer size 2048 as input.
'''
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

# This line closes the socket. The process then terminates.
clientSocket.close()
