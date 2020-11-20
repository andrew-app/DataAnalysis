import pandas as pd

df = pd.read_csv(r"C:\Users\andre\Documents\SentdexDA\datasets\avocado.csv")

graph_df = pd.DataFrame()

region_df = df.copy()[ df['region'] == "California" ]

cali = region_df[["Date","AveragePrice"]]

x="jan"
cali.insert(0,"Month",x)

cali = region_df[["Date","AveragePrice"]]

for month in region_df['Date']:
    if (month[6] == "1"):
        
        print(x)

