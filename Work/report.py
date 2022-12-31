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
            holding['shares']=int(row[1])
            holding['price']=round(float(row[2]),2)
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
total_prices=read_prices('Work/Data/prices.csv')
list_portfolio=read_portfolio('Work/Data/portfolio.csv')
for portfolio in list_portfolio:
    gain_loss=portfolio['price']-total_prices[portfolio['name']]
    print('Stock:',portfolio['name'],'----Gain or Loss:',round(gain_loss),2)


