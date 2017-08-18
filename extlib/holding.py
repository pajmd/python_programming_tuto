#holding.py

class Holding(object):
	def __init__(self, name, price, shares, date):
		self.name = name
		self.data = date
		self.shares = shares
		self.price = price

	def cost(self):
		return self.shares * self.price

	def sell(self, nshares):
		self.shares -= nshares


import csv
def read_portfolio(filename):
	portfolio = []
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			h = Holding(row[0],row[1],row[2],row[3])
			portfolio.append(h)
	return portfolio


if __name__ == '__main__' :
	portfolio = read_portfolio('../portfolio.csv')
	print (portfolio)
	

