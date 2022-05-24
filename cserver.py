import socket
print("The UDP-based Chat server is running.");
#select a server port
server_port = 12000
#create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind the server to the localhost at port server_port
server_socket.bind(('',server_port))
#ready message
print('Chat server running on port ', server_port)

#Now the loop that actually listens from clients
#The same server socket serves all clients here

c1add = ('localhost', 13000);
c2add = ('localhost', 14000);
while True:
    #cadd below is the client process address
    cmsg, cadd = server_socket.recvfrom(2048)
    cmsg = cmsg.decode()
    if cadd[1]==13000:
        print("Message forwarded to client 2.");
        server_socket.sendto(cmsg.encode(),c2add)
    elif cadd[1]==14000:
        print("Message forwarded to client 1.");
        server_socket.sendto(cmsg.encode(),c1add)
        
	

