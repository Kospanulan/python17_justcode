import pandas as pd

df = pd.read_csv(
    r'data/people.csv'
)

# df = df.set_index(df.Name)
# print(df)

# res = df.loc[df["Gender"] == "Male"]
# res = df.loc[df["Gender"] == "Female"]
# res = df.loc[df["Age"] > 30]
# res = df.loc[df["Age"] < 30]
res = df.loc[df["Name"].str.contains("l")]
# res = df.loc[df["Gender"].str.startswith("F")]
# res = df.loc[df["Gender"].str.endswith("ale")]

print(res)

res.to_csv("data/new.csv")

