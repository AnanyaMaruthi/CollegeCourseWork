from socket import *

serverName = "10.124.6.72"
serverPort = 7000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print("Server is ready..")
while True:
    filename, clientAddress = serverSocket.recvfrom(2048)
    filename = filename.decode()
    try:
        file = open(filename, "r")
        data = file.read()    
    except:
        data = "File not found"
    serverSocket.sendto(data.encode(), clientAddress)

