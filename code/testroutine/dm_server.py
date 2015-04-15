import os
import enum

class server:

	def __init__ (self, Name, Ip, statistics, Os = None):
		self.__name = Name
		self.__ip = Ip
		self.__services = []
		self.__statistics = statistics
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
		if self.__pingProb <= 1 and self.__pingProb >= 0.8:
			self.__state = 1
		elif self.__pingProb <= 0.79 and self.__pingProb >= 0.41:
			self.__state = 2
		elif self.__pingProb <= 0.4 and self.__pingProb >= 0:
			self.__state = 3

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

	def getStatistic(self):
		return self.__statistic
