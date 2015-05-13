import cgi
import ccookie
from string import Template
import sys
import configparser
import os

class index:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__loadConfigFile()
		self.__cookieExist()
		self.__pfx = None
		self.__useCookie = 0
		self.__cookie = ccookie.ccookie()

	def loadConfig(self):
		self.__loadConfigFile()
		self.__loadDefaultConf('DEFAULT')
		self.__loadIndexConf()

	def __cookieExist(self):
		if 'HTPP_COOKIE' in os.environ:
			self.__cookieExist = 1
		else:
			self.__cookieExist = 0

	def useCookie(self):
		pass

	def __loadConfigFile(self):
		self.__cfg.read('conf.ini')

	def __loadDefaultConf(self, section):
		for key in self.__cfg[section]:
			pass

	def __loadIndexConf(self):
		pass

	def loadElements(self):
		pass

	def render(self):
		pass

	def printPage(self):
		pass

	def connectData(self):
		pass

	def getPage(self):
		return self.__page

	def parseArg(self, argv):
		if len(argv)>1:
			a = 0
			for i in argv:
				if a== 0:
					a +=1
				else:
					code, arg = i.split('=')
					if code == '-pfx':
						self.__pfx = arg

if __name__ == "__main__":
	a = index.index()
	a.parseArg(sys.argv)
	a.loadConfig()
	a.useCookie()
	a.connectData()
	a.render()
	a.printPage()
