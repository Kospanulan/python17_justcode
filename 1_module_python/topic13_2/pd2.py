import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [1, 32, 99]
})

df["C"] = df["A"] + df["B"]

# df["D"] = pd.Series([0, 0, 0])
# df["F"] = [0, 0, 0, 0]

print(df)




