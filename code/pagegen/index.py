#!/usr/bin/python3
import cgi
import ccookie
from string import Template
import sys
import configparser
import os

import cgitb
cgitb.enable()

class index:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__cookieExist()
		self.__pfx = None
		self.__useCookie = 0

	def loadConfig(self):
		self.__loadConfigFile()
		self.__loadDefaultConf('DEFAULT')
		self.__loadIndexConf()

	def __cookieExist(self):
		if 'HTPP_COOKIE' in os.environ:
			self.__cookieExist = 1
		else:
			self.__cookieExist = 0

	def useCookie(self):
		if self.__useCookie:
			pass

	def __loadConfigFile(self):
		self.__cfg.read('conf.ini')

	def __loadDefaultConf(self, section):
		for key in self.__cfg[section]:
			if key == 'pfx':
				self.__pfx = self.__getConfItem(section, key)
			elif key == 'trp':
				self.__trp = self.__getConfItem(section, key)
			elif key == 'cookie':
				self.__useCookie = int(self.__getConfItem(section, key))
			elif key == 'mysql':
				self.__mysql = int(self.__getConfItem(section, key))

	def __getConfItem(self, section, key):
		return self.__cfg[section][key]

	def __loadIndexConf(self):
		section = 'INDEX'
		for key in self.__cfg[section]:
			if key == 'title':
				self.__title = self.__getConfItem(section, key)

	def loadElements(self):
		pass

	def render(self):
		self.__body = self.__body.substitute(header=self.__header, wrapper=self.__contentwrapper, footer=self.__footer)
		self.__page = self.__page.substitute(body=self.__body, title = self.__title)

	def printPage(self):
		self.__page.replace('\n',' ')
		self.__page.replace('\t',' ')
		print('Content-Type: text/html; charset=iso8858-15\n\n'+self.__page)

	def connectData(self):
		pass

	def getPage(self):
		return self.__page

	def loadTemplates(self):
		self.__page = Template(open('template/head.html').read().replace('\n', ' '))
		self.__body = Template(open('template/body.html').read().replace('\n', ' '))
		self.__header = Template(open('template/header.html').read().replace('\n', ' '))
		self.__contentwrapper = Template(open('template/contentwrapper.html').read().replace('\n', ' '))
		self.__footer = Template(open('template/footer.html').read().replace('\n', ' '))

if __name__ == "__main__":
	a = index()
	a.loadConfig()
	a.useCookie()
	a.connectData()
	a.loadTemplates()
	a.loadElements()
	a.render()
	a.printPage()
