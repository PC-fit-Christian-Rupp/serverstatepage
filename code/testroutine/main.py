import sys
import configparser
import os

class main:
	
	def __init__(self, path = None):
		self.__cfg = configparser.ConfigParser()
		self.__path = "conf.ini"
		self.__section = 'DEFAULT'

	def parsearg(self, argv):
		if len(argv)>1:
			a = 0
			for i in argv:
				if a==0:
					a=1
				else:
					code, arg = i.split('=')
					if code == '-p':
						if os.path.isfile(arg):
							self.__path = arg
						else:
							print(arg, "is a not existing file!")
					elif code == '-pfx':
						self.__pfx = arg

	def readConfig(self):
		self.__cfg.read(self.__path)

	def loadConfig(self):
		self.__loadDefault()
		if self.__mysql == 1:
			self.__loadMysql()

	def __loadDefault(self):
		self.__mysql = 0

	def __loadMysql(self):
		pass

if __name__ == "__main__":
	Main = main()
	Main.parsearg(sys.argv)
	Main.readConfig()
	Main.loadConfig()
