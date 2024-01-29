import pandas as pd


df = pd.read_csv("data/sales.csv")

# res = df.groupby("Product")[["Quantity", "Price"]].sum()
grouped = df.groupby("Product")["Quantity"].sum()
grouped2 = df.groupby("Product")[ ["Quantity", "Price"] ].sum()


print(df)
print("================================================================")
print(grouped)
print("================================================================")
print(grouped2)
