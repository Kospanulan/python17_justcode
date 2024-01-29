import pandas as pd


df = pd.read_csv("data/sales.csv")

res = df.groupby("Product")[["Quantity", "Price"]].sum()
# res = df.groupby("Product")[["Quantity"]].sum()


print(res)
print(" max() =================================")
# print(res.index)
print(res.max())
print(" idxmax() =================================")
print(res.idxmax())
print(" res.loc[ res['Quantity'].idxmax() ] =================================")

result = res.loc[ res['Quantity'].idxmax() ]
print(result)



