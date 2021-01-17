import socket
import threading
import os
import pyfiglet as py
from termcolor  import  colored

myprotocol = socket.AF_INET
myFamilyNetworkName = socket.SOCK_DGRAM

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.system("cls")
results = py.figlet_format( "UDP CHAT APP", font = "bubble" )
print(colored(results, 'green'))

serverip =input("\n\t\tEnter SERVER IP : ")
serverport = 1111

clientip =input("\n\t\tEnter CLIENT IP : ")
clientport =  1111

s.bind((serverip, serverport))

def send():
	while True:
		msg = input("your msg: ").encode()
		s.sendto(msg,(clientip,clientport))
		if msg.decode() == "exit" or msg.decode() == "quit":
			os._exit(1)

def recv():
	msg = s.recvfrom(1024)
	if msg[0].decode() == "quit" or msg[0].decode() == "exit":
		os._exit(1)
	print('\n\t\t\t\t\t\tReceived msg: '+ msg[0].decode())
	
os.system('color 4')

t1 = threading.Thread(target=recv)
t1.start()

t1 = threading.Thread(target=send)
t1.start()

while True:
	t2 = threading.Thread(target=recv)
	t2.start()