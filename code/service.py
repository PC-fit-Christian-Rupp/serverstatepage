

class service:

	def __init__(self, port = None, name = None):
		if port and port > 0:
			self.__port = port
		else:
			#TODO raise exception
			return None
		if name:
			self.__name = name
		else:
			self.__name = 'Service Name missing'
