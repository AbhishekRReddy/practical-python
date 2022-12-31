def pcost(filename):
    file=open(filename,'rt')
    headers=next(file).split(',')
    total_cost=0
    for line in file:
        row=line.split(',')
        total_cost+=int(row[1])*float(row[2])
    return total_cost

cost=pcost('Work/Data/portfolio.csv')
print(f'Total Cost: {cost:0.2f}')
