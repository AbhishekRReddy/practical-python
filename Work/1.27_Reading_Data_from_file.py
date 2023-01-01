import csv
import sys
def pcost(filename):
    file=open(filename)
    rows=csv.reader(file)
    headers=next(rows)
    total_cost=0
    for rowno,row in enumerate(rows,start=1):
        record=dict(zip(headers,row))
        try:
            share=int(record['shares'])
            price=float(record['price'])
            total_cost+=share*price
        except ValueError:
            print(f'Row {rowno}:Couldnt convert:{row}')
    return total_cost
if(len(sys.argv)==2):
    filename=sys.argv[1]

else:
    filename='Work/Data/portfoliodate.csv'

cost=pcost(filename)
print(f'Total Cost: {cost:0.2f}')
