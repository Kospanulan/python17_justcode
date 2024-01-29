import pandas as pd

df = pd.read_csv("data/sales.csv")

res = df.groupby("Product")[["Quantity", "Price"]].sum()

result = res.loc[res['Quantity'].idxmax()]
print(result)
