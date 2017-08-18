#subclass.py
import dateobj

class SubDate(dateobj.Date):
	def stuff(self):
		print('stuff')

d = SubDate.today();
print(d.year)
