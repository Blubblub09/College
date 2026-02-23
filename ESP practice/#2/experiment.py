import matplotlib.pyplot as plt
import numpy as np
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

df1 = df[['Date', 'GBP - EUR', 'GBP - USD']]
df1["Date"] = pd.to_datetime(df1["Date"], dayfirst = True, format = "mixed")
print(df1.head())

start_date = "2024-04-01"
end_date = "2024-05-01"


filtered_df = df1[(df1["Date"] >= start_date) & (df1["Date"] <= end_date)]

plt.grid()
subtitle = f" (between {start_date} and {end_date})"
plt.title(f"Date vs Currency conversion {subtitle}")
plt.plot(df1['GBP - EUR'], label='GBP - EUR', marker = "", color = "red", linestyle = "dashed", linewidth = 2)
plt.plot(df1['GBP - USD'], label='GBP - USD', marker = "", color = "blue", linestyle = "dashed", linewidth = 2)
plt.plot(filtered_df['GBP - EUR'], label='GBP - EUR', marker = "", color = "green", linestyle = "solid", linewidth = 5)
plt.plot(filtered_df['GBP - USD'], label='GBP - USD', marker = "", color = "yellow", linestyle = "solid", linewidth = 5)
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.savefig('ESP practice/#2/exchange_rates.png', dpi = 400)