
import pandas as pd


df = pd.read_csv("data/sales.csv")

df["Overall"] = df['Quantity'] * df['Price']
# res = df["Overall"].sum()
res = df.sum()

print(res)


