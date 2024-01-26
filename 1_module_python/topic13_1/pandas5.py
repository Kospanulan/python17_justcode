import pandas as pd

df = pd.read_csv(
    r'data/people.csv'
)

# df = df.set_index(df.Name)
# print(df)

# print(df.loc["Alice": "David"])
# print(df.loc["Alice": "David", "Name":"Gender"])
# print(df.loc[:, "Name":"Gender"])
# print(df.loc[:, ["Name", "Gender"]])


print(df.loc[0:3])
print("------------------")
print(df.iloc[0:3])
