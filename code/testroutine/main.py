import sys
import configparser

class main:
	
	def __init__(self, path = None):
		self.__cfg = configparser.ConfigParser()
		self.__path = "conf.ini"

	def parsearg(self, argv):
		pass

	def readConfig(self):
		self.__cfg.read(self.__path)

if __name__ == "__main__":
	Main = main()
	Main.parsearg(sys.argv)
	Main.readConfig()
	Main.loadDefault()
	if len(sys.argv)==2:
		path = sys.argv[1]
		if (os.path.exists(path))
			Main = main(path)
	else:
		Main = main()
