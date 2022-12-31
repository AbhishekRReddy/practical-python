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
            holding={}
            holding['name']=row[0]
            holding['shares']=row[1]
            holding['price']=row[2]
            portfolio.append(holding)
        return portfolio

def read_prices(filename):
    prices={}
    file=open(filename,'rt')
    rows=csv.reader(file)
    header=next(rows)
    for row in rows:
        try:
            prices[row[0]]=float(row[1])       
        except IndexError:
            print('Found empty line')
        
    return prices
total_prices=read_prices('Work/Data/prices.csv')
print(total_prices)