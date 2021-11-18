import csv

import pandas as pd
from datetime import datetime
# INPUT PAIR NAME
COINPAIR = 'comp-ust'


filelist = []

FileOpen = '1inch-usd.csv'
header = ['time','open','close','high','low','volume','Unnamed: 0']

# DELETES FIRST COLUMN
df = pd.read_csv('1inch-ust-tester.csv')
# If you know the name of the column skip this
first_column = df.columns[0][0:]
# Delete first
df = df.drop([first_column], axis=1)
csvfile = 'comp-ust'
df.to_csv(COINPAIR + '.csv', index=False)

# CREATES LIST THAT TRANSFORMS UNIX TO DATE
with open(FileOpen,'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        ktime = row[0]
        newtime = int(str(ktime)[:-3])
        filelist.append(datetime.fromtimestamp(newtime))

# WRITING DATE INTO CSV FILE
with open('CONVERTED\\' + 'CONVERTED-' + COINPAIR + '.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(header)
    for val in filelist:
        writer.writerow([val])



