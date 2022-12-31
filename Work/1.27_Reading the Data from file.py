file=open('Work/Data/portfolio.csv','rt')
headers=next(file).split(',')
total_cost=0
for line in file:
    row=line.split(',')
    total_cost+=int(row[1])*float(row[2])
print(f'Total Cost: {total_cost:0.2f}')
print(row)