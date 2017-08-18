"""
This is a module docstring
"""
v1='stuff'
v2= 1234
v3 = 23.54354
def func():
	"""
	summary function docstring

	More explantion docstring
	"""
	out = open('printtofile.txt', 'w')
	print('{:>10s} {:>10d} {:>10.2f}'.format(v1,v2,v3), file=out)
	out.close()

func()

print('suf {:>10s}'.format('stuff'))