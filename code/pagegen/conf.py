import configparser
import os

class conf:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('conf.ini')
		self.__cookieexist()
		self.__pfx = None
		self.__useCookie = 0
		self.__usecookie()
		self.__loadDefaultConf('DEFAULT')
		if self.__mysql:
			self.__loadMysql('MYSQL')

	def __connectData(self):
		pass

	def __parsePath(self):

	def __usecookie(self):
		if self.__useCookie:
			pass

	def __loadDefaultConf(self, section):
		for key in self.__cfg[section]:
			if key =='pfx':
				self.__pfx = self.__getConfItem(section, key)
			elif key == 'trp':
				self.__trp = self.__getConfItem(section, key)
			elif key == 'cookie':
				self.__useCookie = int(self.__getConfItem(section, key))
			elif key == 'mysql':
				self.__mysql = int(self.__getConfItem(section, key))
			elif key == 'rootpath':
				self.__rootpath = self.__getConfItem(section, key)

	def getRootPath(self):
		return self.__rootpath

	def __getConfItem(self, section, key):
		return self.__cfg[section][key]

	def __cookieexist(self):
		if 'HTTP_COOKIE' in os.environ:
			self.__cookieExist = 1
		else:
			self.__cookieExist = 0

	def getIndex(self):
		section = 'INDEX'
		for key in self.__cfg[section]:
			if key == 'title':
				title = self.__getConfItem(section, key)
			elif key == 'headertitle':
				headertitle = self.__getConfItem(section, key)
		return (title, headertitle)
