import sys
import configparser
import os
import time

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
							print('['+time.ctime()+'] '+arg+ " is a not existing file!", file=sys.stderr)
					elif code == '-pfx':
						self.__pfx = arg

	def setPfx(self, pfx):
		self.__pfx = pfx

	def readConfig(self):
		self.__cfg.read(self.__path)

	def loadConfig(self):
		self.__loadDefault()
		if self.__mysql == 1:
			self.__loadMysql()

	def __loadDefault(self):
		if (not os.path.isfile(self.__cfg[self.__section]['testinifile'])):
			print('['+time.ctime()+'] No Testini File!', file=sys.stderr)
		else:
			self.__testinifile = self.__cfg[self.__section]['testinifile']
		if (not os.path.exists(self.__cfg[self.__section]['rootpath'])):
			print('['+time.ctime()+'] No existing root path!', file=sys.stderr)
		else:
			self.__rootpath = self.__cfg[self.__section]['rootpath']
		if (isinstance(int(self.__cfg[self.__section]['usemysql']), int)):
			self.__mysql = self.__cfg[self.__section]['usemysql']
			self.__section = 'MYSQL'
		else:
			self.__mysql = 0

	def __loadMysql(self):
		self.__connection = self.__cfg[self.__section]['connection']
		self.__database = self.__cfg[self.__section]['database']
		self.__user = self.__cfg[self.__section]['user']
		self.__pwd = self.__cfg[self.__section]['pwd']
		self.__statistics = self.__cfg[self.__section]['statistics']

if __name__ == "__main__":
	Main = main()
	Main.parsearg(sys.argv)
	Main.readConfig()
	Main.loadConfig()
