import configparser

class loadConfig:

	def __init__(self):
		self.__default = 'DEFAULT'
		self.__loadConfig()
		self.__countServer = self.__loadCountServer()

	def __loadConfig(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('config.ini')

	def __loadCountServer(self):
		return self.__cfg[self.__default]['CountServer']
