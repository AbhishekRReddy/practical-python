import csv
import sys
def pcost(filename):
    import report
    portfolio=report.read_portfolio(filename)
    total_cost=0
    for i,stock in enumerate(portfolio,start=1):
        try:
            share=int(stock['shares'])
            price=float(stock['price'])
            total_cost+=share*price
        except ValueError:
            print(f'Row {i}:Couldnt convert:{stock}')
    return total_cost
