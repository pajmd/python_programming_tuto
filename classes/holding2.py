#holding.py

class Holding(object):
	def __init__(self, name, date, price, shares):
		self.name = name
		self.date = date
		self.price = price
		self.shares = shares

	def cost(self):
		return self.shares * self.price

	def read_portfolio(filename):

