#!/usr/bin/python3

import configparser
import cgitb
import loadConfig

cgitb.enable()

class web():

	def __init__(self, page = NONE):
		if page.equals(NONE):
			self.__page = 'WebElements'
		else:
			self.__page = page
		self.__setElementsFile()
		self.__loadHeader()
		self.__loadBody()
		if page.equals('impressum'):
		else:
			self.__loadServiceBody()
			self.__loadPageBody()
			self.__loadElements()

	# Loads the elements file for the webpage
	def __setElementsFile(self):
		self.__ele = configparser.ConfigParser()
		self.__ele.read('web.ini')

	def __loadHeader(self):
		self.__header = self.__ele[self.__page]['header']

	def __loadBody(self):
		self.__body = self.__ele[self.__page]['body']

	def __loadBlock(self):
		self.__block = self.__ele[self.__page]['block']

	def __loadElements(self):
		self.__green = self.__ele[self.__page]['ElementGreen']
		self.__yellow = self.__ele[self.__page]['ElementYellow']
		self.__red = self.__ele[self.__page]['ElementRed']
		self.__black = self.__ele[self.__page]['ElementBlack']