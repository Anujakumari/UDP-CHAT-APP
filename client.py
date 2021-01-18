# importing required modules
import socket
import threading
import os
import pyfiglet as py
from termcolor  import  colored

os.system('color 4')

myprotocol = socket.AF_INET
myFamilyNetworkName = socket.SOCK_DGRAM

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system("cls")
results = py.figlet_format( "UDP CHAT APP", font = "bubble" )
print(colored(results, 'red'))

serverip =input("\n\t\tEnter SERVER IP : ")
serverport = 1111

clientip =input("\n\t\tEnter CLIENT IP : ")
clientport =  1111

#binding IP and PORT of system
s.bind((serverip, serverport))


# For Sending Message..
def send():
	while True:
		msg = input(" ").encode()
		s.sendto(msg,(clientip,clientport))
		if msg.decode() == "exit" or msg.decode() == "bye":
			os._exit(1)

# For Receiving Message..
def recv():
	while True:
		msg = s.recvfrom(1024)
		if msg[0].decode() == "bye" or msg[0].decode() == "exit":
			os._exit(1)
		print('\n\t\t\t\t\t\tReceived msg: '+ msg[0].decode())
	


# Applying Multi-Threading Concept...
recv = threading.Thread(target=recv)
send = threading.Thread(target=send)

recv.start()
send.start()