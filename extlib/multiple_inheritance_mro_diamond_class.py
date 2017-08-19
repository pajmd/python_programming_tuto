#
#
# This example runs in 2.7 beacuse of the way super is called:
#
# it shows the order of inheritance goes from left to right then up to the super class
# MRO Method Resolution Order
#
# Interesting enough the QuotedMixin and StarMixin don't even inherit of nothing
#
# Also in python 3 super would be call as super().
#
# See learning python 5th edition: chap 32: Coupling: Application to mix-in classes

# multiple_inheritance_mro_diamond_class.py

class BaseFormatter(object):
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

class TextFormatter(BaseFormatter):
    def headings(self, headers):
        print('Formatting the header')

    def row(self, rowdata):
        print('TextFormatter formatting a row')


class QuotedMixin(object):
    def row(self, rowdata):
        print('QuotedMixin formatting a row')
        super(QuotedMixin, self).row(rowdata)


class StarMixin(object):
    def row(self, rowdata):
        print('StarMixin formatting a row')
        super(StarMixin, self).row(rowdata)


class MergeFormat(QuotedMixin, StarMixin, TextFormatter):
    pass

merge_format = MergeFormat()
print(MergeFormat.__mro__)
merge_format.row(['stuf'])

star_mixin = StarMixin()
try:
    star_mixin.row(['sdsd'])
except AttributeError as e:
    print('Expecting AttributeError: super object has no attribute row'.format(e))