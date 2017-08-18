# table.py

def print_table(objs, cols):
	'''
	priint a nice table with column names and values for each object passed in the list objs
	'''
	for col in cols:
		print ('{:>10s}'.format(col), end=' ') #end pevents \n
	print()
	for obj in objs:
		for col in cols:
			print('{:>10s}'.format(str(getattr(obj, col))), end=' ') 
		print()


def print_table(objs, cols, formatter):
	'''
	priint a nice table with column names and values for each object passed in the list objs
	'''
	formatter.headings(cols)

	for obj in objs:
		rowdata = [str(getattr(obj,col)) for col in cols]
		#print('rowdata: ', rowdata)
		formatter.row(rowdata)

import formatter
class TextFormatter(formatter.Formatter):
	def headings(self, headers):
		for col in headers:
			print ('{:>10s}'.format(col), end=' ') #end pevents \n
		print()

	def row(self, rowdata):
		print('formatter ')
		for item in rowdata:
			print ('{:>10s}'.format(item), end=' ') #end pevents \n
		print()

class QuotedMixin(object):
	def row(self, rowdata):
		print('quoted mixin ')
		quoted = ['"{}"'.format(d) for d in rowdata]
		super().row(quoted)


class StarMixin(object):
	def row(self, rowdata):
		print('star mixin ')
		quoted = ['*{}'.format(d) for d in rowdata]
		super().row(quoted)

class MergeFormat(QuotedMixin, StarMixin, TextFormatter ):
	pass



#export PYTHONPATH=../classes
if __name__ == '__main__':
	import holding

	portfolio = holding.read_portfolio('../portfolio.csv')
#	print ('My portfolio: ', portfolio)

#	print_table(portfolio, ['name', 'price'])
	formatter = TextFormatter()
	print_table(portfolio, ['name', 'price'], formatter)

	mergeFormat = MergeFormat()
	print_table(portfolio, ['name', 'price'], mergeFormat)
