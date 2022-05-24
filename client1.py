import socket

#the server name and port client wishes to access
server_name = 'localhost'
server_port = 12000
my_port=13000
#create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind this client to port number 13000
client_socket.bind(('',my_port))

while True:
    #some work
    msg = input("You say: ");
    #send the message  to the udp server
    client_socket.sendto(msg.encode(),(server_name, server_port))
    #return values from the server
    msg, sadd = client_socket.recvfrom(2048)
    msg = msg.decode()
    print("Client 2 says: ", msg)
    

client_socket.close()
