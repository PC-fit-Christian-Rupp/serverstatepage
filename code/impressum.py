#!/usr/bin/python3

import configparser
import cgitb

cgitb.enable()

class impressum():

	def __init__(self):
		self.__setELemnentFile()

	def __setElementFIle(self):
		self.__ele = configparser.ConfigParser()
		self.__ele.read('web.ini')		

