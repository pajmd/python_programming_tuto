#dateobj

class Date(object):
	def __init__(self, year, month , day):
		self.year = year
		self.month = month
		self.day = day

	@classmethod
	def from_string(cls, s): #The class is pass in the cls argument
		parts = s.split('-')
		return cls(int(parts[0]), int(parts[1]), int(parts[2]))

	@classmethod
	def today(cls): #no need to hard code class Date in the method
		import time
		t = time.localtime()
		return cls(t.tm_year, t.tm_mon, t.tm_mday)


