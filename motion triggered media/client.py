#client.py
#---------
#Mike Moniz

import socket
import sys
import string

def sendMessage(ip, port, message):
	print (" ip: " + ip)
	print (" port: " + str(port))

	#connect to the server
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.settimeout(10) #wait 10 seconds for the server
		print (" connecting...")
		s.connect((ip,int(port)))
		
		print (" ready to send data")
		
		message = message + "#" #escape terminal
		
		s.send( message.encode('utf-8'))

		print (" sent data")
	except KeyboardInterrupt:
		print (" Quit")
	except Exception as e:
		print (e)
	finally:
		s.close()

#example usage
#
#ip = sys.argv[1] #"192.168.0.11"
#port = sys.argv[2] #29876
#message = sys.argv[3] #"opensesame"

#sendMessage(ip, port, message)
