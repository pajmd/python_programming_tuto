import csv
# from sys import argv
import sys


def get_portfolio_list(portfolio_file, errLevel):
    '''
    Reads a portfolio from a csv file a returns a list of tuples
    '''
    with open(portfolio_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        portfolio = []
        for row in csvreader:
            try:
                print(";".join(row))
                row[1] = float(row[1])
                row[2] = int(row[2])
                holding = tuple(row)
                portfolio.append(holding)
            except ValueError as errReported:
                print('Error level:', errLevel)
                if errLevel == 'warn':
                    print('Bad row', row)
                    print('Got error:', errReported)
                elif errLevel == 'raise':
                    raise
                else:
                    pass
        return portfolio


# def get_portfolio_dict(portfolio_file,*, errLevel): # * only in python3
def get_portfolio_dict(portfolio_file, errLevel):
    '''
    Reads a portfolio from a csv file a returns a list of dictionaries
    '''
    with open(portfolio_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        print('Header:', header)
        portfolio = []
        for rownum, row in enumerate(csvreader, start=1):
            try:
                print(";".join(row))
                row[1] = float(row[1])
                row[2] = int(row[2])
                holding = {
                    header[0]: row[0],
                    header[1]: row[1],
                    header[2]: row[2],
                    header[3]: row[3],
                }
                portfolio.append(holding)
            except ValueError as errReported:
                print('Error level:', errLevel)
                if errLevel == 'warn':
                    print('ROW num:', rownum, ' Bad row', row)
                    print('Got error:', errReported)
                elif errLevel == 'raise':
                    raise
                else:
                    pass
        return portfolio


if sys.argv[1] == 'list':
    portfolio = get_portfolio_list('portfolio.csv', errLevel='warn')
    print('Protfolio list', portfolio)
    total = 0.0
    for name, price, share_num, date in portfolio:
        total += price * share_num
    print('Total value', total)

if sys.argv[1] == 'dict':
    portfolio = get_portfolio_dict('portfolio.csv', errLevel='warn')
    print('Protfolio dict', portfolio)
    print('Total value', sum(share['price'] * share['shares'] for share in portfolio))


    def getName(holding):
        return holding['name']


    portfolio.sort(key=getName)
    print('Sorted portfolio:', portfolio)
    portfolio.sort(key=lambda holding: holding['name'])
    print('Sorted portfolio with lambda:', portfolio)

    import itertools

    for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name']):
        print(name)
        for item in items:
            print('  ', item)

    # build a dict per name - also showing I can split the line with <cr>
    by_name = {name: list(items)
               for name, items in
               itertools.groupby(portfolio, key=lambda holding: holding['name'])}
    print('All msft:', by_name['msft'])
