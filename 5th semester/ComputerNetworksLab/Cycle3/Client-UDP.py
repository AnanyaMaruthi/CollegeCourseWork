from socket import *
serverName = "127.0.0.1"
serverPort = 7000
clientSocket = socket(AF_INET, SOCK_DGRAM)
filename = input("Enter filename")
clientSocket.sendto(filename.encode(), (serverName, serverPort))
content, serverAddress = clientSocket.recvfrom(4096)
print(content.decode())
clientSocket.close()
