import configparser
import server
import service
import HTTP

class loadConfig:

	def __init__(self):
		self.__default = 'DEFAULT'
		self.__lst = []
		self.__loadConfig()
		self.__countServer = self.__loadCountServer()
		self.__readData()

	def __loadConfig(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('config.ini')

	def __loadCountServer(self):
		return self.__cfg[self.__default]['CountServer']

	def __readData(self):
		for i in self.__countServer:
			self.__loadServer(i)

	def __loadServer(self, numb):
		tmp = server.server(self.__cfg[self.__default][str(numb)+'.IP'],self.__cfg[self.__default][str(numb)+'.Name'])
		for i in self.__cfg[self.__default][str(numb)+'.CountService']:
			self.__loadService(i, tmp)
		self.__lst.add(tmp)

	def loadData(self):
		for i in self.__lst:
			i.loadData()

