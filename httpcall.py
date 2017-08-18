from urllib import request
import sys

#if len(sys.argv) < 2:
#	raise SystemExit('Not enough arguments')

#http://www.google.com/search?q=stuff
query = sys.argv[1]
print(query)
urlpath = 'http://www.google.com/s'
urlquery = 'http://www.google.com/search?q='+query
print(urlpath)
print(urlquery)
u = request.urlopen(urlquery)
data = u.read()
print(data)

