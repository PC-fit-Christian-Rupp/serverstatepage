#!/usr/bin/python3

import configparser
import cgitb
import loadConfig

cgitb.enable()

class web():

	def __init__(self, page = None):
		if page:
			self.__page = page
		else:
			self.__page = 'WebElements'
		self.__setElementsFile()
		self.__loadHeader()
		self.__loadBody()
		if self.__page == 'IMPRESSUM':
			self.__loadAdress()
			self.__loadErk()
		else:
			self.__loadBlock()
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

	def __loadAdress(self):
		self.__adress = self.__ele[self.__page]['adress']

	def __loadErk(self):
		self.__erk = self.__ele[self.__page]['erk']

	def getHeader(self):
		return self.__header

	def getBody(self):
		return self.__body

	def getAdress(self):
		return self.__adress

	def getErk(self):
		return self.__erk

	def getBlock(self):
		return self.__block

	def getGreen(self):
		return self.__green

	def getYellow(self):
		return self.__yellow

	def getRed(self):
		return self.__red

	def getBlack(self):
		return self.__black


