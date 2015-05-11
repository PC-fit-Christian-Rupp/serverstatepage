import cgi
import ccookie
from string import Template
import sys

class index:

	def __init__(self):
		pass

	def __loadDefaultConf(self):
		pass

	def __loadIndexConf(self):
		pass

	def parseArg(self, argv):
		if len(argv)>1:
			a = 0
			for i in argv:
				if a== 0:
					a +=1
				else:
					code, arg = i.split('=')
					if code == '-pfx':
						self.__pfx = arg

if __name__ == "__main__":
	a = index.index()

