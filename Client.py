#CLIENT SIDE (PYTHON)

import socket
import time

HOST = "10.144.134.213"     # Symbolic name meaning all available interfaces
PORT = 5007               # Arbitrary non-privileged port

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
sock.connect(server_address)
print ('Connected')
try:
    
    # Send data
    msg = input("6 Digit Code: ")
    sock.send(msg.encode())
    print ('Sending Code...')

    # Look for the response
    answer = sock.recv(1024).decode()
    #print(answer)       
    if answer == 'Gucci':
    	print ("Authorized")

    else:
        print('Not Authorized')

finally:
    sock.close()
