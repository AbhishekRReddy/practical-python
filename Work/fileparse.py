# fileparse.py
#
# Exercise 3.3
def parse_csv(filename,select=None,types=None,has_headers=False):
    import csv
    with open(filename) as f:
        rows=csv.reader(f)
        if(has_headers):
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
            if(types):
                row=[func(val) for func,val in zip(types,row)]
            if(has_headers):
                record=dict(zip(headers,row))
            else:
                record=tuple(row)
            records.append(record)
    return records
