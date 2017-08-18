#child1.py
from parent import Parent;

class Child1(Parent):
	def spam(self):
		print('From child val', self.val)

	def othermethod(self):
		print('othermethod')


if __name__ == '__main__':
	c = Child1(654)
	c.spam();