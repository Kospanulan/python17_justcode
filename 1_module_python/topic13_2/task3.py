import pandas as pd

df = pd.read_csv("data/sales.csv")

grouped = df.groupby('Product').agg(
    {
        'Price': ['mean', 'sum', 'max', 'min'],
    }
)

# print(grouped)
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
print(grouped)
