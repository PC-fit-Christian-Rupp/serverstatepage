import ops
import os
import time
import sys
import server
import configparser

class wrap_ini:

	def __init__(self, path):
		if os.path.isfile(path):
			self.__path = path
		else
			print('['+time.ctime()+'] This is not a file!', file=sys.stderr)
		self.__cfg = configparser.ConfigParser()
		self.__def = 'DEFAULT'

	def loadconf(self):
		self.__cfg.read(self.__path)
		self.__servercount = int(self._cfg[self.__def]['SERVER_COUNT'])

	def load(self):
		pass

	def __loadServer(self):
		pass

	def getData(self):
		return self.__data
