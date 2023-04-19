import socket

serverName = socket.gethostname()
IP = socket.gethostbyname(serverName)
serverPort = 12000

print(IP)

# the server creates a TCP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# associate the server port number and server name with this socket
serverSocket.bind((IP, serverPort))
'''
With TCP, serverSocket will be our welcoming socket. 
After establishing this welcoming door, we will wait and listen for some client to knock on the door

This line has the server listen for TCP connection requests from the client.
The parameter specifies the maximum number of queued connections (at least 1).
'''
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    '''
    When a client knocks on this door, the program invokes the accept() method for
    serverSocket, which creates a new socket in the server, called connectionSocket,
    dedicated to this particular client. The client and server then complete the handshaking, 
    creating a TCP connection between the client’s clientSocket and the server’s connectionSocket
    '''
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(f"Received data from {addr}: {sentence}")
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
    if sentence == "close":
        break
