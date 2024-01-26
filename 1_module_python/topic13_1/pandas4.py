import pandas as pd

df = pd.read_csv(
    r'data/people.csv'
)

# print(df.iloc[2])
print(df.iloc[1:3])

# print(df.iloc[0:3, 0:2])
# print(df.iloc[:, 0])
# print(df.Name)


