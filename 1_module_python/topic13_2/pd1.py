import pandas as pd


df = pd.read_csv("data/sales.csv")

df["Overall"] = df['Quantity'] * df['Price']
df["Month"] = df['Date'].str[:7]

print(df)
# print("=================================================")
# res = df.groupby("Product").sum()
# print(res.loc[:, ['OrderID', 'Overall', 'Category']])

print("=================================================")
# res = df.groupby("Product")[['Overall']].sum()
res = df.groupby("Month")[['Overall']].sum()
print(res)

# print(res.loc[:, ['OrderID', 'Overall', 'Category']])




