#!/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))

rawSocket.bind(("ens33", socket.htons(0x0806)))

packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06')

rawSocket.send(packet + "Hello World")
