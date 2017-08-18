import portfoliopkg

portfolio = portfoliopkg.readcsv('portfolio.csv', [str,float,int,str], errLevel='pass')
print ('My portfolio: ', portfolio)