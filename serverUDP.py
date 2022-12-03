#server side connection - UDP
from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) #bind server to port, always listens to 12001
print 'The server is ready to receive'
while 1: #server needs to be always on, runs while loop forever
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.upper() #convert message to upper,also store in modifiedMessage
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) #sends modified message to client


