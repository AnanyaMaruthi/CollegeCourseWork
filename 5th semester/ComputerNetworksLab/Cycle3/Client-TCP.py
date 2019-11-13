from socket import *
serverPort = 6000
serverName = "127.0.0.1"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
filename = input("Enter the name of the file ")
clientSocket.send(filename.encode())
message = clientSocket.recv(1024)
print(message.decode())
clientSocket.close()
