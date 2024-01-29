import pandas as pd


df = pd.read_csv("data/sales.csv")

# res = df.groupby("Product")[["Quantity", "Price"]].sum()
grouped = df.groupby("Product")[["Quantity"]].sum()

res = grouped.sort_values('Quantity', ascending=False)  # ascending, descending  # asc, desc
print(res.iloc[:5])
