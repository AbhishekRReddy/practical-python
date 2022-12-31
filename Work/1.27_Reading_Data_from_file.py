import csv
import sys
def pcost(filename):
    file=open(filename)
    rows=csv.reader(file)
    headers=next(rows)
    total_cost=0
    for row in rows:
        try:
            total_cost+=int(row[1])*float(row[2])
        except ValueError:
            print('Invalid Line.....Skipping')
    return total_cost
if(len(sys.argv)==2):
    filename=sys.argv[1]

else:
    filename='Work/Data/portfolio.csv'

cost=pcost(filename)
print(f'Total Cost: {cost:0.2f}')
