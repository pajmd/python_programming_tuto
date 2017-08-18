#child2.py
from parent import Parent;

class Child2(Parent):
	def spam(self):
		print('spam from child val', self.val)
		super(Child2, self).spam();

	def othermethod(self):
		print('othermethod')


if __name__ == '__main__':
	c = Child2(654)
	c.spam();