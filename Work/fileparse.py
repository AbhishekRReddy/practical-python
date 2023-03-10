# fileparse.py
#
# Exercise 3.3
def parse_csv(any_iterable,select=None,types=None,has_headers=True,delimit=',',silence_errors=True):
    import csv
    if(type(any_iterable) is str):
        raise SystemExit('Please provide iterable rather than fielname')
    if(not has_headers and select):
        raise RuntimeError('Select argument requires headers')
    rows=csv.reader(any_iterable,delimiter=delimit)
    if(has_headers):
        headers=next(rows)
    if(select):
        positions=[headers.index(column) for column in select]
        headers=select
    records=[]
    
    for row_no,row in enumerate(rows,start=1):
        if(not row):
            continue
        if(select):
            row=[row[i] for i in positions]
        if(types):
            try:
                row=[func(val) for func,val in zip(types,row)]
            except ValueError as e:
                if(not silence_errors):
                    print('Row ',row_no,"Couldn't convert",row)
                    print('Row ',row_no, e)
                continue
        if(has_headers):
            record=dict(zip(headers,row))
        else:
            record=tuple(row)
        records.append(record)
    return records
