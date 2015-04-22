import enums
import os
import time
import sys
import dm_server
import configparser

class wrap_ini:

	def __init__(self, path):
		if os.path.isfile(path):
			self.__path = path
		else:
			print('['+time.ctime()+'] This is not a file!', file=sys.stderr)
		self.__cfg = configparser.ConfigParser()
		self.__def = 'DEFAULT'

	def loadconf(self):
		self.__cfg.read(self.__path)
		self.__servercount = int(self._cfg[self.__def]['SERVER_COUNT'])

	def load(self):
		self.__data = []
		for i in range(self.__servercount):
			self.__data.append(self.__loadServer(i))

	def __loadServer(self, i):
		j = str(i)
		name = self.__cfg[j]['NAME']
		ip = self.__cfg[j]['IP']
		statisics = int(self.__cfg[j]['STATISTICS'])
		opersys = ops.ops.XP.parse(self.__cfg[j]['OS'])
		server = dm_server.dm_server(name, ip, statistics, opersys)
		services_count = int(self.__cfg[j]['SERVICE_COUNT'])
		#LOad Service for this Server
		for i in range(services_count):
			pass
		return server

	def getData(self):
		return self.__data
