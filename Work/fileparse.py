# fileparse.py
#
# Exercise 3.3
def parse_csv(filename):
    import csv
    with open(filename) as f:
        rows=csv.reader(f)
        headers=next(rows)
        records=[]
        for row in rows:
            if(not row):
                continue
            record=dict(zip(headers,row))
            records.append(record)
    return records
