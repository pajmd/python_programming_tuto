import csv
import sys

def readcsv(file, types, errLevel):
	'''
	Reads a csv file, applies conversion and returns a dictionary list
	'''
	with open(file, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		header = next(csvreader)
		entrylist = []
		for rownum, row in enumerate(csvreader, start=1):
			try:
				row = [typefunc(entry) for typefunc, entry in  zip(types,row)]
				holding = {name: val for name, val in zip(header, row) }
				#holding = dict( zip(header, row) )
				entrylist.append(holding)
			except ValueError as errReported:
				if errLevel == 'warn':
					print('ROW num:', rownum,' Bad row', row)
					print('Got error:', errReported)
				elif errLevel == 'raise':
					raise
				else:
					pass
		return entrylist

if __name__ == '__main__':
	entryList = readcsv('portfolio.csv', [str,float,int,str], errLevel='warn')
	print (entryList)

print(__name__, 'loaded')