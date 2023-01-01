# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    portfolio=[]
    with open(filename,'rt') as file:
        rows=csv.reader(file)
        header=next(rows)
        for row in rows:
            record=dict(zip(header,row))
            holding={}
            holding['name']=record['name']
            holding['shares']=int(record['shares'])
            holding['price']=round(float(record['price']),2)
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    prices={}
    file=open(filename,'rt')
    rows=csv.reader(file)
    for row in rows:
        try:
            prices[row[0]]=float(row[1])       
        except IndexError:
            print('Found empty line')
        
    return prices

def make_report(portfolio,prices):
    stock_status=[]
    for stock in portfolio:
        stock_status.append((stock['name'],stock['shares'],prices[stock['name']],
        -stock['price']+prices[stock['name']]))
    return stock_status
        
total_prices=read_prices('Work/Data/prices.csv')
list_portfolio=read_portfolio('Work/Data/portfolio.csv')
report=make_report(list_portfolio,total_prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
dash='-'*10
print((dash+' ')*len(headers))
for name,shares,price,change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



