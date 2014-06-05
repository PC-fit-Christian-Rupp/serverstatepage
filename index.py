#!/usr/bin/python3

import configparser

class index():

	def __init__(self):
		self.__setElementsFile()
		self.__loadHeader()
		self.__loadBody()
		self.__loadServiceBody()
		self.__loadPageBody()

	# Loads the elements file for the webpage
	def __setElementsFile(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('web.ini')

	def __loadHeader(self):
		self.__header = self.cfg['DEFAULT']['header']

	def __loadBody(self):
		self.__body = self.cfg['DEFAULT']['body']

	def __loadBlock(self):
		self.__block = self.cfg['DEFAULT']['block']

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
