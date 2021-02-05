# Im tired of copy/pasting pdf tables for taxes
# 2021 _crushton

import tabula
import sys
import pandas as pd
import numpy as np
import re
#data = [] # list of three-value lists

# Collect filename and pages from sys.argv
inFile = sys.argv[1] 
outFile = sys.argv[2]
#bank = sys.argv[3]

# regex
  # detect date without repeat ##/##  ([0-1][1-9]/[0-3][0-9]\s)(?=[^0-1][^1-9][^/][^0-3][^0-9])
  # rest of text ([a-zA-Z0-9\s.\-]+$) or .*
  # $ value (^\$[0-9]+\.[0-9][0-9])

# Citibank hard coded statments
def trimCols(table): # Dec 2020 (guess:F) Nov 2020 (guess:T)
  cols = len(table.columns)
  if cols == 4: # keep cols 0,2
    return table.iloc[:, [True, False, True, False]]
  elif cols == 5: # keep cols 0,3 
    return table.iloc[:, [True, False, False, True, False]]
  elif cols == 6: # keep cols 1,2,5 
    return table.iloc[:, [False, True, True, False, False, True]]

def cleanCols(data):
  data.columns = ["Description", "Amount"]
  tmp = pd.DataFrame() #index=np.arrange(0, len(data.index))) 
  tmp = data.iloc[:,0].str.extract(r'([0-1][0-9]/[0-3][0-9]\s)(?=[^0-1][^1-9][^/][^0-3][^0-9])(.*$)')
  data['Date'] = tmp.iloc[:,0]
  data['Description'] = tmp.iloc[:,1]
  data = data[['Date', 'Amount', 'Description']]
  return data

# Input: index of table in tables and boolean array of target cols in table
# Output: reordered dataframe with three target cols 
def hasTwo(idx, ary):
  return cleanCols(tables[idx].iloc[:, ary])

def hasThree(idx, ary):
  tmp = pd.DataFrame()
  tmp = tables[idx].iloc[:, ary]
  row = tmp.columns
  tmp.loc[len(tables[idx].index)] = row
  tmp.columns = ["Date", "Description", "Amount"]
  return tmp[['Date', 'Amount', 'Description']]

def citiBank():
  data = pd.concat(list((trimCols(table) for table in tables)), ignore_index=True)
  return cleanCols(data)

def citiBank2():
  row = [] 
  lst = []
  lst.append(hasTwo(0, [True, True, False]))
  lst.append(hasThree(1, [False, True, True, False, False, False, True]))
  lst.append(hasThree(3, [False, True, True, False, False, True]))
  return pd.concat(lst)

def firstTest():
  for table in tables:
    print(table) 

# Switching statement depending on bank
def dataframeFromBank():
  if bank == "citi":
    return citiBank()
  elif bank == "boa":
    return bankOfAmerica()
  elif bank == "marcus":
    return goldmanSacchs()
  elif bank == "ccu":
    return californiaCreditUnion()

# Generate individual tables (play with guess T/F)
tables = tabula.read_pdf(inFile, pages='all', multiple_tables=True, guess=True) # type list
#firstTest()
#citiBank2()
# Generate csv
# tabula.convert_into(inFile, outFile, pages='all', guess=False)
citiBank2().dropna().to_csv(outFile)

