import socket
import threading
import os
import pyfiglet as py
from termcolor  import  colored

myprotocol = socket.AF_INET
myFamilyNetworkName = socket.SOCK_DGRAM

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system("clear")
results = py.figlet_format( "UDP CHAT APP", font = "bubble" )
print(colored(results, 'red'))

serverip =input("\n\t\tEnter SERVER IP : ")
serverport = 1111

clientip =input("\n\t\tEnter CLIENT IP : ")
clientport =  1111

s.bind((serverip, serverport))

def send():
	while True:
		msg = input("Your Message: ").encode()
		s.sendto(msg,(clientip,clientport))
		if msg.decode() == "exit" or msg.decode() == "bye":
			os._exit(1)

def recv():
	msg = s.recvfrom(1024)
	if msg[0].decode() == "bye" or msg[0].decode() == "exit":
		os._exit(1)
	print('\n\t\t\t\t\t\tReceived Message: '+ msg[0].decode())


t1 = threading.Thread(target=recv)
t1.start()

t1 = threading.Thread(target=send)
t1.start()

while True:
	t2 = threading.Thread(target=recv)
	t2.start()