#!/usr/bin/python3

import configparser

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

	# Loads the elements file for the webpage
	def __setElementsFile(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('web.ini')

	def __loadHeader(self):
		self.__header = self.__cfg['WebElements']['header']

	def __loadBody(self):
		self.__body = self.__cfg['WebElements']['body']

	def __loadBlock(self):
		self.__block = self.__cfg['WebElements']['block']

	def __loadElements(self):
		self.__green = self.__cfg['WebElements']['ElementGreen']
		self.__yellow = self.__cfg['WebElements']['ElementYellow']
		self.__red = self.__cfg['WebElements']['ElementRed']
		self.__black = self.__cfg['WebElements']['ElementBlack']

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
