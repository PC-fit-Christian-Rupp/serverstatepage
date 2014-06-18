#!/usr/bin/python3

import configparser
import cgitb

cgitb.enable()

class impressum():

	def __init__(self):
		self.__setELemnentFile()

	def __setElementFile(self):
		self.__ele = configparser.ConfigParser()
		self.__ele.read('web.ini')

	def generatePage(self):
		self.__htdoc = NONE

	def view(self):
		print(self.__htdoc)

if __name__ == '__main__':
	page =	impressum()
	page.generatePage()
	page.view()

