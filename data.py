import pandas as pd
import numpy as np

data = open('./data/KRAKEN_ETHUSD, 60.csv', 'r')
ETHUSD = pd.read_csv(data)
average_price = []

print(ETHUSD[2:3].close)

#for i in range (0, 300):
#  if (i > 4):
#        average_price.append((ETHUSD))

# import ETHUSD 60 data
# 300 hours worth of data
# calculate moving average for the data
