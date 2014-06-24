#!/usr/local/bin/python3

import configparser
import cgitb
import loadConfig
import web

cgitb.enable()

# Generate the index page with the states
class index:

	# Generates this object
	def __init__(self):
		self.__web = self.__getWeb()
		self.__cfg = self.__getCfg()

	def __getWeb(self):
		return web.web()

	def __getCfg(self):
		return loadConfig.loadConfig()

	def loadData(self):
		self.__cfg.loadData()

	def generatePage(self):
		self.__page = ''

	def __generateServices(self):
		return None

	def __generatePages(self):
		return None

	def view(self):
		print(self.__page)

if __name__ == "__main__":
	Index = index()
	Index.loadData()
	Index.generatePage()
	Index.view()
