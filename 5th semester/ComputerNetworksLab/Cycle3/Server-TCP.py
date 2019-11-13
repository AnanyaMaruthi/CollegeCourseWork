from socket import *

serverName = "10.124.6.72"
serverPort = 7000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is ready to receive ")
while True:
	connectionSocket, addr = serverSocket.accept()
	fileName = connectionSocket.recv(1024)
	fileName = fileName.decode()
	try:
	    file = open(fileName, "r")
	    data = file.read()
	    
	except:
	    data = "File not found"
	connectionSocket.send(data.encode())
	connectionSocket.close()
