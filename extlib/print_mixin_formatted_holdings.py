# print_formatted_holdings.py
#
# This example should be run in 3.5 because of the definition of the
# bas abstrct class
#
# See learning python 5th edition: chap 32: Coupling: Application to mix-in classes

def print_table(objs, cols):
    '''
    priint a nice table with column names and values for each object passed in the list objs
    '''
    for col in cols:
        print('{:>10s}'.format(col), end=' ')  # end pevents \n
    print()
    for obj in objs:
        for col in cols:
            print('{:>10s}'.format(str(getattr(obj, col))), end=' ')
        print()




import base_formatter


class TextFormatter(base_formatter.Formatter):
    def headings(self, headers):
        for col in headers:
            print('{:>10s}'.format(col), end=' ')  # end pevents \n
        print()

    def row(self, rowdata):
        print('formatter ')
        for item in rowdata:
            print('{:>10s}'.format(item), end=' ')  # end pevents \n
        print()


class QuotedMixin(object):
    def row(self, rowdata):
        print('quoted mixin ')
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class StarMixin(object):
    def row(self, rowdata):
        print('star mixin ')
        quoted = ['*{}'.format(d) for d in rowdata]
        super().row(quoted)


class MergeFormat(QuotedMixin, StarMixin, TextFormatter):
    pass


def print_table(objs, cols, formatter):
    '''
    priint a nice table with column names and values for each object passed in the list objs
    '''
    formatter.headings(cols)

    for obj in objs:
        rowdata = [str(getattr(obj, col)) for col in cols]
        # print('rowdata: ', rowdata)
        formatter.row(rowdata)


# export PYTHONPATH=../classes
if __name__ == '__main__':
    import holding

    portfolio = holding.read_portfolio('../portfolio.csv')
    # #	print ('My portfolio: ', portfolio)
    #
    # #	print_table(portfolio, ['name', 'price'])
    # formatter = TextFormatter()
    # print_table(portfolio, ['name', 'price'], formatter)

    print()
    print("Using Merge mixin - "*5)
    try:
        text_formatter = base_formatter.Formatter()
    except TypeError as e:
        print('Expected error bc an abstrct class can not be instantiated: {}\n'.format(e))
    mergeFormat = MergeFormat()
    print('Order of the inheritance search: {}'.format(mergeFormat.__mro__))
    print_table(portfolio, ['name', 'price'], mergeFormat)
