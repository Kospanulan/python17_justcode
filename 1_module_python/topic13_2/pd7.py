import pandas as pd

df = pd.read_csv("data/sales.csv")

# grouped = df.groupby('Product')[['Price']].mean()  # avg()

# grouped = df.groupby('Product').agg(
#     {
#         'Price': 'mean',
#         'Quantity': 'sum'
#     }
# )

grouped = df.groupby('Product').agg(
    {
        # 'Price': [('A', 'mean'), ('C', 'sum')],
        # 'Quantity': [('B', 'mean'), ('D', 'sum')]
        'Price': ['mean', 'sum', 'max', 'min'],
        # 'Quantity': ['mean', 'sum']
    }
)

# print(grouped.Quantity)
grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
# res = [col for col in grouped.columns.values]
print(grouped)
