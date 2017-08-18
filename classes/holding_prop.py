#holding.py

class Holding(object):
	def __init__(self, name, price, shares, date):
		self.name = name
		self.data = date
		self.shares = shares
		self.price = price

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, newprice):
		self._price = newprice

	def cost(self):
		return self.shares * self.price

	def sell(self, nshares):
		self.shares -= nshares
