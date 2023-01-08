class TableFormatter:
    def headings(self,headers):
        '''
        print the table headers
        '''
        raise NotImplementedError
    def row(self,rowdata):
        '''
        Print the single row of the table data
        '''
        raise NotImplementedError
    
class TextTableFormatter(TableFormatter):
    def headings(self,headers):
        for h in headers:
            print(f'{h:>10s}',end=" ")
        print()
        print(('-'*10+' ')*len(headers))
    
    def row(self,rowdata):
        for column in rowdata:
            print(f'{column:>10s}',end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))
    def row(self, rowdata):
        print(','.join(rowdata))