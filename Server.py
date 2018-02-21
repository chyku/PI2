#SERVER SIDE (PYTHON)

import socket
import time

import os

HOST = ''
PORT = 5007

#create a socket on the network using port 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#name of the host (router, unless it has no name, then return IP address)
HOSTNAME = socket.gethostname()
server_address = (HOST, PORT)
print('Hostname: %s' % HOSTNAME)
print(HOST)
print('starting up on %s port %s' % (server_address[0], server_address[1]))

#binds to the host and port
s.bind(server_address)
#listens to the bound host's port
#waits for (1) connection
s.listen(1)
print('listening for a connection...')

while(True):
    try:
        #if a connection` is found, accept it and create (object, string)
        (CONNECTION, ADDRESS) = s.accept()
        print(ADDRESS)
        print('connection found...')
        #receive the data (up to 3 bytes or 24 bits or 2^24)
        
        data = CONNECTION.recv(1024).decode("utf-8")
        print(data)
        if data == '54':
            msg = 'Authorized'
            print('Authorized Connection')

            CONNECTION.send(msg.encode("utf-8"))
            #GPIO.output(7, GPIO.HIGH)
            #GPIO.output(11, GPIO.LOW)
        elif(data == 'stop'):
            CONNECTION.close()
            break;

        CONNECTION.close()

    except KeyboardInterrupt:
       s.close()
       CONNECTION.close()


if __name__ == "__main__":
    find_env()
