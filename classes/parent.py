#parent.py

class Parent(object):
	def __init__(self, val):
		self.val = val

	def spam(self):
		print(self.val)


if __name__ == '__main__':
	p = Parent(32)
	p.spam();