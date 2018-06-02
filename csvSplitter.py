import pandas as pd
import sys

# msft = pd.read_csv(sys.argv[1])
# row_count = sum(1 for row in msft)
# print(row_count)
#print(msft.head())
for i,chunk in enumerate(pd.read_csv(sys.argv[0], chunksize=500000)):
    chunk.to_csv('chunk{}.csv'.format(i))
