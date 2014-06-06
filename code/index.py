#!/usr/bin/python3

import configparser
import cgitb
import loadConfig

cgitb.enable()

# Generate the index page with the states
class index():

	# Generates this object
	def __init__(self):
		self.__setElementsFile()
		self.__loadHeader()
		self.__loadBody()
		self.__loadServiceBody()
		self.__loadPageBody()
		self.__loadElements()
		self.__cfg = self.__getCfg()

	# Loads the elements file for the webpage
	def __setElementsFile(self):
		self.__ele = configparser.ConfigParser()
		self.__ele.read('web.ini')

	def __loadHeader(self):
		self.__header = self.__ele['WebElements']['header']

	def __loadBody(self):
		self.__body = self.__ele['WebElements']['body']

	def __loadBlock(self):
		self.__block = self.__ele['WebElements']['block']

	def __loadElements(self):
		self.__green = self.__ele['WebElements']['ElementGreen']
		self.__yellow = self.__ele['WebElements']['ElementYellow']
		self.__red = self.__ele['WebElements']['ElementRed']
		self.__black = self.__ele['WebElements']['ElementBlack']

	def __getCfg(self):
		return loadConfig.loadConfig()

	def loadData(self):
		return NONE

	def generatePage(self):
		return NONE

	def __generateServices(self):
		return NONE

	def __generatePAges(self):
		return NONE

	def view(self):
		print(NONE)

if __name__ == "__main__":
	Index = index()
	Index.loadData()
	Index.generatePage()
	Index.view()
