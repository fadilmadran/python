#!/usr/bin/python

import sys,socket

def main(args):
	UDP_IP = "10.90.120.35"
	UDP_PORT = 6666
	#message = "SPARELOC#1551895101000#41.072957#29.015860#2.50#50.3#1.85#5.90"
	message = "SPARELOC#1551895101000#41.076432#29.014411#2.50#44.3#1.85#5.90"
	print "UDP target IP:", UDP_IP
	print "UDP target port:", UDP_PORT
	if len(sys.argv) > 1:
		message = sys.argv[1]
	print "message:", message

	sock = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
	sock.sendto(message, (UDP_IP, UDP_PORT))


main(sys.argv)
