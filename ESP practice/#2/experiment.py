import matplotlib as plt
import pandas as pd
 
df = pd.read_csv("ESP practice/#2/data.csv")

'''
#df.info()
 
df.head()
 
 
# get_conversion_rate()
currency = 'GBP - EUR'
conversion_rate = round(df[currency].iloc[-1],2)
print("conversion_rate = ", conversion_rate)
 '''

df1 = df[['Date', 'USD - GBP', 'GBP - USD']]
print(df1.head())