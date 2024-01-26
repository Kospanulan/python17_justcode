import pandas as pd

df = pd.read_csv(
    r'data/people.csv',
    # header=None,
    # names=['n1', 'n2', 'n3', 'n4']
)

# df = pd.read_csv(
#     r'data/people2.csv',
#     sep=';',
#     # delimiter=';'
# )

# print(df.Name,Age,Gender,City)
# print(df["Name,Age,Gender,City"])
print(df)
