import sys
import configparser

class main:
	
	def __init__(self, path = None):
		self.__cfg = configparser.ConfigParser()
		self.__path = "conf.ini"

	def parsearg(self, argv):
		if len(argv)>1:
			a = 0
			for i in argv:
				if a==0:
					a=1
				else:
					code, arg = i.split('=')
					if code is p:
						if os.file.exists(arg):
							self.__path = arg
					elif code is pfx:
						self.__pfx = arg

	def readConfig(self):
		self.__cfg.read(self.__path)

if __name__ == "__main__":
	Main = main()
	Main.parsearg(sys.argv)
	Main.readConfig()
	Main.loadDefault()
