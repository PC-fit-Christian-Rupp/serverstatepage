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
