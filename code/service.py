import configparser

class service:

	def __init__(self, cfg, i, pfx):
		self.__port = cfg[pfx+'SERVICE'][i+'Port']
		self.__name = cfg[pfx+'SERVICE'][i+'Name']
		self.__countObjects = cfg[pfx+'SERVICE'][i+'CountObjects']
		self.__state = 1
		if self.__countObjects > 0:
			self.__readData(cfg)

	def getState(self):
		return self.__state

