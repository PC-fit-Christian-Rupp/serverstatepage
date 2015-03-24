import sys
import configparser

class main:
	
	def __init__(self, path = None):
		self.__cfg = configparser.ConfigParser()
		if path:
			self.__cfg.read(path)
		else:
			self.__cfg.read("conf.ini")

if __name__ == "__main__":
	if len(sys.argv)==2:
		path = sys.argv[1]
		if (os.path.exists(path))
			Main = main(path)
	else:
		Main = main()
