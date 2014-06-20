#!/usr/local/bin/python3

import configparser
import cgitb
import web

cgitb.enable()

class impressum():

	def __init__(self):
		self.__web = self.__getWeb()

	def __getWeb(self):
		return web.web('IMPRESSUM')

	def generatePage(self):
		self.__htdoc = NONE

	def view(self):
		print(self.__htdoc)

if __name__ == '__main__':
	page =	impressum()
	page.generatePage()
	page.view()

