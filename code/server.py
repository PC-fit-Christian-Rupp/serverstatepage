import os
import sys
import ipaddress

class server:

	def __init__(self, ip, name = None):
		self.__ip = ipaddress.ip_address(ip)
		if name:
			self.__name = name
		else:
			self.__name = 'Missing Server Name'
		self.__color = '#FFFF00'

	def getName(self):
		return self.__name

	def scan(self):
		response = os.system("ping -c 1 " + str(self.__ip))
		if response == 0:
			self.__color = '#00FF00'
		else:
			self.__color = '#FF0000' 
		return response

	def getColot(self):
		return self.__color

