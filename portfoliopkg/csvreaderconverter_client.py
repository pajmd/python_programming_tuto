#import csvreaderconverter
# would work if csvreaderconverter_client.py was imported
from . import csvreaderconverter

portfolio = csvreaderconverter.readcsv('portfolio.csv', 
	[str,float,int,str], errLevel='pass')
print ('My portfolio: ', portfolio)