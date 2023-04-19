import socket

serverName = socket.gethostname()
serverPort = 12000

'''
This line creates the client’s socket, called clientSocket. The first parameter
again indicates that the underlying network is using IPv4. The second parameter 
indicates that the socket is of type SOCK_STREAM, which means it is a TCP socket
(rather than a UDP socket)
'''
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
The below line initiates the TCP connection between the client and server. The parameter
of the connect() method is the address of the server side of the connection. After
this line of code is executed, the three-way handshake is performed and a TCP connection is established between 
the client and server.
'''
clientSocket.connect((serverName, serverPort))

'''
The above line sends the sentence through the client’s socket and into the TCP
connection. Note that the program does not explicitly create a packet and attach the
destination address to the packet, as was the case with UDP sockets. Instead the client program simply drops the bytes 
in the string sentence into the TCP connection. The client then waits to receive bytes from the server.
'''
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
