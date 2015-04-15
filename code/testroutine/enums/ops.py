from enum import Enum
import osFamily

class ops(Enum):
	
	# WINDOWS Desktop Family
	XP = ("XP", 5.1, osFamily.osFamily.WINDOWS)
	VISTA = ("Vista", 6.0, osFamily.osFamily.WINDOWS)
	SEVEN = ("7", 6.1, osFamily.osFamily.WINDOWS)
	EIGHT = ("8", 6.2, osFamily.osFamily.WINDOWS)
	EIGHTONE = ("8.1", 6.3, osFamily.osFamily.WINDOWS)

	# WINDOWS Server Family
	TWOTHOUSANDTHREE = ("2003", 5.3, osFamily.osFamily.WINDOWSSERVER)
	TWOTHOUSANDEIGHT = ("2008", 6.0, osFamily.osFamily.WINDOWSSERVER)
	TWOTHOUSANDEIGHTR2 = ("2008 R2", 6.1, osFamily.osFamily.WINDOWSSERVER)
	TWOTHOUSANDWTWELVE = ("2012", 6.2, osFamily.osFamily.WINDOWSSERVER)

	# UBUNTU Desktop Family
	PRECISEPANGOLIN = ("Precise Pangolin", 12.0405, osFamily.osFamily.UBUNTU)
	QUANTALQUETZAL = ("Quantal Quetzal", 12.10, osFamily.osFamily.UBUNTU)
	RAIRINGRINGTAIL = ("Rairing Ringtail", 12.04, osFamily.osFamily.UBUNTU)
	SAUCYSALAMANDER = ("Saucy Salamander", 13.04, osFamily.osFamily.UBUNTU)
	TRUSTYTAHR = ("Trusty Tahr", 14.0402, osFamily.osFamily.UBUNTU)
	UTOPICUNICORN = ("Utopic Unicorn", 14.10, osFamily.osFamily.UBUNTU)
	VIVIDVERVET = ("Vivid Veret", 15.04, osFamily.osFamily.UBUNTU)

	# UBUNTU SERVER Family
	PRECISEPANGOLINSERVER = ("Precise Pangolin", 12.0405, osFamily.osFamily.UBUNTUSERVER)
	QUANTALQUETZALSERVER = ("Quantal Quetzal", 12.10, osFamily.osFamily.UBUNTUSERVER)
	RAIRINGRINGTAILSERVER = ("Rairing Ringtail", 12.04, osFamily.osFamily.UBUNTUSERVER)
	SAUCYSALAMANDERSERVER = ("Saucy Salamander", 13.04, osFamily.osFamily.UBUNTUSERVER)
	TRUSTYTAHRSERVER = ("Trusty Tahr", 14.0402, osFamily.osFamily.UBUNTUSERVER)
	UTOPICUNICORNSERVER = ("Utopic Unicorn", 14.10, osFamily.osFamily.UBUNTUSERVER)
	VIVIDVERVETSERVER = ("Vivid Veret", 15.04, osFamily.osFamily.UBUNTUSERVER)

	# LINUX Kernel Family Desktop
	TWOFOUR = ("Kernel", 2.4, osFamily.osFamily.LINUX)
	TWOFIVE = ("Kernel", 2.5, osFamily.osFamily.LINUX)
	TWOSIX = ("Kernel", 2.6, osFamily.osFamily.LINUX)
	THREE = ("Kernel", 3.0, osFamily.osFamily.LINUX)
	THREEONE = ("Kernel", 3.1, osFamily.osFamily.LINUX)
	THREETWO = ("Kernel", 3.2, osFamily.osFamily.LINUX)
	THREETHREE = ("Kernel", 3.3, osFamily.osFamily.LINUX)
	THREEFOUR = ("Kernel", 3.4, osFamily.osFamily.LINUX)
	THREEFIVE = ("Kernel", 3.5, osFamily.osFamily.LINUX)
	THREESIX = ("Kernel", 3.6, osFamily.osFamily.LINUX)
	THREESEVEN = ("Kernel", 3.7, osFamily.osFamily.LINUX)
	THREEEIGHT = ("Kernel", 3.8, osFamily.osFamily.LINUX)
	THREENINE = ("Kernel", 3.9, osFamily.osFamily.LINUX)
	THREETEN = ("Kernel", 3.10, osFamily.osFamily.LINUX)
	THREEELEVEN = ("Kernel", 3.11, osFamily.osFamily.LINUX)
	THREETWELVE = ("Kernel", 3.12, osFamily.osFamily.LINUX)
	THREETHIRTEEN = ("Kernel", 3.13, osFamily.osFamily.LINUX)
	THREEFOURTEEN = ("Kernel", 3.14, osFamily.osFamily.LINUX)
	THREEFIVTEEN = ("Kernel", 3.15, osFamily.osFamily.LINUX)
	THREESIXTEEN = ("Kernel", 3.16, osFamily.osFamily.LINUX)
	THREEEIGHTEEN =  ("Kernel", 3.18, osFamily.osFamily.LINUX)
	THREENINETEEN = ("Kernel", 3.19, osFamily.osFamily.LINUX)
	FOUR = ("Kernel", 4.0, osFamily.osFamily.LINUX)

	# LINUX Kernel Family SERVER
	TWOFOURSERVER = ("Kernel", 2.4, osFamily.osFamily.LINUXSERVER)
	TWOFIVESERVER = ("Kernel", 2.5, osFamily.osFamily.LINUXSERVER)
	TWOSIXSERVER = ("Kernel", 2.6, osFamily.osFamily.LINUXSERVER)
	THREESERVER = ("Kernel", 3.0, osFamily.osFamily.LINUXSERVER)
	THREEONESERVER = ("Kernel", 3.1, osFamily.osFamily.LINUXSERVER)
	THREETWOSERVER = ("Kernel", 3.2, osFamily.osFamily.LINUXSERVER)
	THREETHREESERVER = ("Kernel", 3.3, osFamily.osFamily.LINUXSERVER)
	THREEFOURSERVER = ("Kernel", 3.4, osFamily.osFamily.LINUXSERVER)
	THREEFIVESERVER = ("Kernel", 3.5, osFamily.osFamily.LINUXSERVER)
	THREESIXSERVER = ("Kernel", 3.6, osFamily.osFamily.LINUXSERVER)
	THREESEVENSERVER = ("Kernel", 3.7, osFamily.osFamily.LINUXSERVER)
	THREEEIGHTSERVER = ("Kernel", 3.8, osFamily.osFamily.LINUXSERVER)
	THREENINESERVER = ("Kernel", 3.9, osFamily.osFamily.LINUXSERVER)
	THREETENSERVER = ("Kernel", 3.10, osFamily.osFamily.LINUXSERVER)
	THREEELEVENSERVER = ("Kernel", 3.11, osFamily.osFamily.LINUXSERVER)
	THREETWELVESERVER = ("Kernel", 3.12, osFamily.osFamily.LINUXSERVER)
	THREETHIRTEENSERVER = ("Kernel", 3.13, osFamily.osFamily.LINUXSERVER)
	THREEFOURTEENSERVER = ("Kernel", 3.14, osFamily.osFamily.LINUXSERVER)
	THREEFIVTEENSERVER = ("Kernel", 3.15, osFamily.osFamily.LINUXSERVER)
	THREESIXTEENSERVER = ("Kernel", 3.16, osFamily.osFamily.LINUXSERVER)
	THREEEIGHTEENSERVER =  ("Kernel", 3.18, osFamily.osFamily.LINUXSERVER)
	THREENINETEENSERVER = ("Kernel", 3.19, osFamily.osFamily.LINUXSERVER)
	FOURSERVER = ("Kernel", 4.0, osFamily.osFamily.LINUXSERVER)

	# MAC Desktop Family
	CHEETAH = ("Cheetah", 10.0, osFamily.osFamily.MAC)
	PUMA = ("Puma", 10.1, osFamily.osFamily.MAC)
	JAGUAR = ("Jaguar", 10.2, osFamily.osFamily.MAC)
	PANTHER = ("Panther", 10.3, osFamily.osFamily.MAC)
	TIGER = ("Tiger", 10.4, osFamily.osFamily.MAC)
	LEOPARD = ("Leopard", 10.5, osFamily.osFamily.MAC)
	SNOWLEOPARD = ("Snow Leopard", 10.6, osFamily.osFamily.MAC)
	LION = ("Lion", 10.7, osFamily.osFamily.MAC)
	MOUNTAINLION = ("Mountain Lion", 10.8, osFamily.osFamily.MAC)
	MAVERICKS = ("Mavericks", 10.9, osFamily.osFamily.MAC)
	YOSEMITE = ("Yosemite", 10.10, osFamily.osFamily.MAC)

	# MAC Server Family
	CHEETAHSERVER = ("Cheetah", 10.0, osFamily.osFamily.MACSERVER)
	PUMASERVER = ("Puma", 10.1, osFamily.osFamily.MACSERVER)
	JAGUARSERVER = ("Jaguar", 10.2, osFamily.osFamily.MACSERVER)
	PANTHERSERVER = ("Panther", 10.3, osFamily.osFamily.MACSERVER)
	TIGERSERVER = ("Tiger", 10.4, osFamily.osFamily.MACSERVER)
	LEOPARDSERVER = ("Leopard", 10.5, osFamily.osFamily.MACSERVER)
	SNOWLEOPARDSERVER = ("Snow Leopard", 10.6, osFamily.osFamily.MACSERVER)
	OSXSERVERONE = ("1.0", 1.0, osFamily.osFamily.MACSERVER)
	OSXSERVERTWO = ("2.0", 2.0, osFamily.osFamily.MACSERVER)
	OSXSERVERTHREE = ("3.0", 3.0, osFamily.osFamily.MACSERVER)
	OSXSERVERFOUR = ("4.0", 4.0, osFamily.osFamily.MACSERVER)

	def getAllClasses(self, classes):
		ret = []
		for i in ops:
			if i.family.osclass.name == classes.name:
				ret.append(i)
		return ret

	def getAllFamily(self, family):
		ret = []
		for i in ops:
			if i.family.family == family.family:
				ret.append(i)
		return ret

	def toString(self):
		if self.family.family == osFamily.osFamily.WINDOWS.family or self.family.family == osFamily.osFamily.WINDOWSSERVER.family:
			return (self.family.family + ' ' + self.os)
		elif self.family.family == osFamily.osFamily.UBUNTU.family or self.family.family == osFamily.osFamily.UBUNTUSERVER.family:
			return (self.family.family + ' ' + str(self.version))
		elif self.family.family == osFamily.osFamily.LINUX.family or self.family.family == osFamily.osFamily.LINUXSERVER.family:
			if self == ops.THREETENSERVER or self == ops.THREETEN:
				return (self.family.family + " " + self.os + " {}0").format(self.version)
			else:
				return self.family.family + ' ' + self.os + ' ' + str(self.version)
		elif self.family.family == osFamily.osFamily.MAC.family:
			if self.version < 10.8:
				return 'MAC '+ self.family.family + ' ' + str(self.version)
			else:
				return self.family.family + ' ' + str(self.version)
		elif self.family.family == osFamily.osFamily.MACSERVER.family:
			if self == ops.CHEETAHSERVER or self == ops.PUMASERVER or self == ops.JAGUARSERVER or self == ops.PANTHERSERVER or self == ops.TIGERSERVER or self ==  ops.LEOPARDSERVER or self == ops.SNOWLEOPARDSERVER:
				return 'MAC '+ self.family.family + ' ' + str(self.version)
			else:
				return self.family.family + ' ' + self.os
				
	def __init__(self, os, version, family):
		self.os = os
		self.version = version
		self.family = family
