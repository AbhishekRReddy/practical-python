# report.py
#
# Exercise 2.4
import csv
import fileparse
import stock
import table_format
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
    for name,shares,price,change in report:
        row_data=[name,str(shares),f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(row_data)

def portfolio_report(portfolio_filename, prices_filename):
    total_prices=read_prices(prices_filename)
    list_portfolio=read_portfolio(portfolio_filename)
    report=make_report(list_portfolio,total_prices)
    formatter=table_format.TextTableFormatter()
    print_report(report,formatter)

def main(filenames):
    portfolio_report(filenames[1],filenames[2])
    
if __name__ == '__main__':
    import sys
    if len(sys.argv)!=3:
        raise SystemExit(f'Usage:{sys.argv[0]}' 'portfolio file price file required')
    main(sys.argv)
