import configparser

class loadConfig:

	def __init__(self):
		self.cfg = configparser.ConfigParser()
		self.cfg.read('config.ini')
