

class HTTP:

	def __init__(self, url):
		self.__url = url
		self.__state = 2

	def scan(self):
		return None

	def getName(self):
		return self.__url

	def getState(self):
		return self.__state

	def loadData(self):
		self.scan()

	def scan(self):
		return None
