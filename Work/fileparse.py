# fileparse.py
#
# Exercise 3.3
def parse_csv(filename,select=None):
    import csv
    with open(filename) as f:
        rows=csv.reader(f)
        headers=next(rows)
        if(select):
            positions=[headers.index(column) for column in select]
            headers=select
        records=[]
        for row in rows:
            if(not row):
                continue
            if(select):
                row=[row[i] for i in positions]
            record=dict(zip(headers,row))
            records.append(record)
    return records
