# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock

def read_portfolio(filename):
    with open(filename) as f:
        portfolio=fileparse.parse_csv(f,types=[str,int,float],has_headers=True,
                                silence_errors=True)
        portfolio=[stock.Stock(d['name'],d['shares'],d['price']) for d in portfolio]
    return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices=fileparse.parse_csv(f,types=[str,float],has_headers=False) 
    return dict(prices)

def make_report(portfolio,prices):
    stock_status=[]
    for stock in portfolio:
        stock_status.append((stock.name,stock.qty,prices[stock.name],
        prices[stock.name]-stock.price))
    return stock_status
        
def print_report(report,formatter):
    formatter.headings(['Name','Shares','Price','Change'])

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    dash='-'*10
    print((dash+' ')*len(headers))
    for name,shares,price,change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    total_prices=read_prices(prices_filename)
    list_portfolio=read_portfolio(portfolio_filename)
    report=make_report(list_portfolio,total_prices)
    print_report(report)

def main(filenames):
    portfolio_report(filenames[1],filenames[2])
    
if __name__ == '__main__':
    import sys
    if len(sys.argv)!=3:
        raise SystemExit(f'Usage:{sys.argv[0]}' 'portfolio file price file required')
    main(sys.argv)
