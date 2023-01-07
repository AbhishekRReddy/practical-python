# report.py
#
# Exercise 2.4
import csv
import fileparse


def read_portfolio(filename):
    portfolio=fileparse.parse_csv(filename,types=[str,int,float],has_headers=True,
                            silence_errors=True)
    return portfolio

def read_prices(filename):
    prices=fileparse.parse_csv(filename,types=[str,float]) 
    return dict(prices)

def make_report(portfolio,prices):
    stock_status=[]
    for stock in portfolio:
        stock_status.append((stock['name'],stock['shares'],prices[stock['name']],
        -stock['price']+prices[stock['name']]))
    return stock_status
        
def print_report(report):
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
    
'''def portfolio_report(portfolio_file, price_file):
    files = [portfolio_file, price_file]
    for name in files:
            print(f'{name:-^43s}')
            portfolio_report(name, 'Data/prices.csv')
            print()'''
