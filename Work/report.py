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
            holding=(row[0],int(row[1]),float(row[2]))
            portfolio.append(holding)
        return portfolio
