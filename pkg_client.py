import portfoliopkg.csvreaderconverter

entryList = portfoliopkg.csvreaderconverter.readcsv('portfolio.csv', 
	[str,float,int,str], errLevel='pass')
print ('My portfolio: ', entryList)