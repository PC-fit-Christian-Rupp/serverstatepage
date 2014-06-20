import configparser

class loadConfig:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('config.ini')
