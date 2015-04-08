import os;

class server:

	def __init__ (self, Name, Ip, Os = None):
		self.__name = Name
		self.__ip = Ip
		self.__services = []
		if Os:
			self.__os = Os
		else:
			self.__os = None

	def addService (self, Service):
		self.__services.append(Service)

	def check (self):
#		for i in self.__services:
#			i.check()
		self.__test()

	def __test(self):
		a = 0
		for i in range(10):
			a += os.system("ping -c 1" + self.__ip)
		self.__pingProb = a/10
		self.__setState()

	def __setState(self):
		pass

	def __checkOs(self):
		pass

	def __checkVersionMac(self):
		pass

	def __checkVersionLinux(self):
		pass

	def __checkVersionWin(self):
		pass

	def getOs(self):
		return self.__os

	def getVersion(self):
		pass

	def getList(self):
		return self.__services

	def getState(self):
		return self.__state

	def getName(self):
		return self.__name

	def getIp(self):
		return self.__ip
