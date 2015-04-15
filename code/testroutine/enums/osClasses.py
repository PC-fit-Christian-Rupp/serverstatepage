from enum import Enum
import re

class osClasses(Enum):
	DESKTOP = 1
	SERVER = 2

	def parse(self, string):
		if re.search(osClasses.DESKTOP.name, string, re.IGNORECASE):
			return osClasses.DESKTOP
		elif re.search(osClasses.SERVER.name, string, re.IGNORECASE):
			return osClasses.SERVER
		else:
			return None
