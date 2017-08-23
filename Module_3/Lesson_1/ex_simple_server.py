#!/usr/bin/env python

# ex_simple_server.py by mariuszha
#
# Purpose:
# Create a simple Echo Server to handle 1 client 
#

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bind_IP = '0.0.0.0'
bind_port = 4444


tcpSocket.bind((bind_IP, bind_port))

tcpSocket.listen(1)


print 'Waiting for a client ...'

(client, (ip, sock)) = tcpSocket.accept()

print 'Receiving connection from %s' % ip

data = client.recv(2048)

client.send('Echo ' + data)

print 'Receiving from the client: %s' % data

client.close()
