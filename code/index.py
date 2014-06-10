#!/usr/bin/python3

import configparser
import cgitb
import loadConfig
import web

cgitb.enable()

# Generate the index page with the states
class index():

	# Generates this object
	def __init__(self):
		self.__web = self.__getWeb()
		self.__cfg = self.__getCfg()

	def __getWeb(self):
		return web.web()

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
