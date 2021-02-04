# Im tired of copy/pasting pdf tables for taxes
# 2021 _crushton

import tabula
import sys
import pandas as pd

data = [] # list of three-value lists


# Collect filename and pages from sys.argv
inFile = sys.argv[1] 
# outFile = sys.argv[2]
# numPages = sys.argv[3]

# Generate csv from pdf in one table
# tabula.convert_into(inFile, outFile, pages='all', guess=False)

# Generate individual tables
tables = tabula.read_pdf(inFile, pages='all', multiple_tables=True, guess=False)
# Print to console
#i = 0

# detect date ([0-1][1-9]/[0-3][0-9]\s/b)
# rest of text ([a-zA-Z0-9\s.\-]+$) 
# $ value (^\$[0-9]+\.[0-9][0-9])
data = tables.str.extract(r'([0-1][1-9]/[0-3][0-9]\s/b)([a-zA-Z0-9\s.\-]+$)(^\$[0-9]+\.[0-9][0-9])')
print data

# Convert data list to df and save as csv
# df = pd.DataFrame(data, columns = ['date', 'amount', 'description'])

  #print(table)
  #i +=1
#print(type(tables))
#print(type(tables[0]))


