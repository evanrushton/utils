# Im tired of copy/pasting pdf tables for taxes
# 2021 _crushton

import tabula
import sys
import pandas as pd
import re
data = [] # list of three-value lists


# Collect filename and pages from sys.argv
inFile = sys.argv[1] 
outFile = sys.argv[2]
# type = sys.argv[3]

# Bank of America hard coded statments
def trimCols(table):
  cols = len(table.columns)
  if cols == 4: # keep cols 0,2
    return(table.iloc[:, [True, False, True, False]])
  elif cols == 5: # keep cols 0,3 
    return(table.iloc[:, [True, False, False, True, False]])

def bankOfAmerica():
  data = pd.concat(list((trimCols(table) for table in tables)), ignore_index=True)
  data.columns = ["Description", "Amount"]
  # detect date ([0-1][1-9]/[0-3][0-9]\s/b)
  # rest of text ([a-zA-Z0-9\s.\-]+$) 
  # $ value (^\$[0-9]+\.[0-9][0-9])
  tmp = pd.DataFrame() 
  tmp  = data.iloc[:,0].str.extract(r'([0-1][1-9]/[0-3][0-9]\s)(?=[^0-1][^1-9][^/][^0-3][^0-9])(.*$)')
  data['Date'] = tmp[0]
  data['Description'] = tmp[1]
  data = data[['Date', 'Amount', 'Description']]
  return data

# Generate csv from pdf in one table
# tabula.convert_into(inFile, outFile, pages='all', guess=False)

# Generate individual tables
tables = tabula.read_pdf(inFile, pages='all', multiple_tables=True, guess=False) # type list

bankOfAmerica().to_csv(outFile)
