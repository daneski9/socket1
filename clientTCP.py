from socket import *
serverName = '127.0.0.1'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = TCP
clientSocket.connect((serverName, serverPort)) #first, establish connection with server
sentence = raw_input('Input lowercase sentence: ')
clientSocket.send(sentence) #.send, because a pipe is already established
modifiedSentence = clientSocket.recv(1024).decode("utf-8")
print 'From Server:', modifiedSentence
clientSocket.close()
 
