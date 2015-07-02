#!/usr/bin/python3
import cgi
import ccookie
from string import Template
import sys
import os
import conf

import cgitb
cgitb.enable()

class index:

	def __init__(self):
		self.__cfg = conf.conf()
		self.__pageValues = self.__cfg.getIndex()

	def loadElements(self):
		pass

	def render(self):
		self.__header = self.__header.substitute(headertitle=self.__pageValues[1])
		self.__body = self.__body.substitute(header=self.__header, wrapper=self.__contentwrapper, footer=self.__footer)
		self.__page = self.__page.substitute(body=self.__body, title = self.__pageValues[0])

	def printPage(self):
		self.__page.replace('\n',' ')
		self.__page.replace('\t',' ')
		print('Content-Type: text/html; charset=iso8858-15\n\n'+self.__page)

	def getPage(self):
		return self.__page

	def loadTemplates(self):
		self.__page = Template(open('template/head.html').read().replace('\n', ' '))
		self.__body = Template(open('template/body.html').read().replace('\n', ' '))
		self.__header = Template(open('template/header.html').read().replace('\n', ' '))
		self.__contentwrapper = Template(open('template/contentwrapper.html').read().replace('\n', ' '))
		self.__footer = Template(open('template/footer.html').read().replace('\n', ' '))

if __name__ == "__main__":
	a = index()i
	a.parsePath()
	a.loadTemplates()
	a.loadElements()
	a.render()
	a.printPage()
