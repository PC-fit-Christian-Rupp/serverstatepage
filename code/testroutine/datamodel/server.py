import os;

class server:

	def __init__ (self, Name, Ip, Os = None):
		self.__name = Name
		self.__ip = Ip

	def addService (self, Service):
		pass

	def check (self):
		pass

	def __test(self):
		a = 0
		for i in range(10):
			a += os.system("ping -c 1" + self.__ip)
		self.__pingProb = a/10

	def __checkOs(self):
		pass

	def __checkVersionMac(self):
		pass

	def __checkVersionLinux(self):
		pass

	def __checkVersionWin(self):
		pass

	def getOs(self):
		pass

	def getVersion(self):
		pass

	def getList(self):
		pass

	def getState(self):
		pass

	def getName(self):
		pass

	def getIp(self):
		return self.__ip
