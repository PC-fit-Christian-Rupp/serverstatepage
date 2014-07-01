import os
import sys
import ipaddress
import service
import configparser

class server:

	def __init__(self, cfg, i):
		self.__pfx = i+'.'
		self.__ip = ipadress.ipadress(cfg[i][self.__pfx+'IP'])
		self.__blackFlag = 0
		self.__lst = []
		if cfg[i][self.__pfx+'Name']:
			self.__name = cff[i][self.__pfx+'Name']
		else:
			self.__name = 'Missing Server Name'
		self.__color = '#FFFF00'
		self.__state = 1

	def getName(self):
		return self.__name

	def scan(self):
		self.__blackFlag = os.system("ping -c 1 " + str(self.__ip))
		if self.__blackFlag == 0:
			self.__state = self.__blackFlag
			self.__color = '#00FF00'
		else:
			self.__color = '#FF0000'
			self.__state = 2
		return response

	def getColor(self):
		return self.__color

	def getState(self):
		return self.__state

	def loadData(self):
		for i in self.__lst:
			i.loadData()
		self.scan()

	def getFlag(self):
		return self.__blackFlag
