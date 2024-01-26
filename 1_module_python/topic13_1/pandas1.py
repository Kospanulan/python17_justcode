import pandas as pd

data = {
    "key": ["value", "value2", "value3"],
    "name": ["Ulan", "Max", "Sasha"],
    "surname": ["Kospan", "Debo", "Petrov"],
    "age": [12, 45, 20],
}

df = pd.DataFrame(data)

# df = df.set_index(df.name)

# s = pd.Series(
#     data=["max", "apple", "banana"],
#     name="Custom Series",
#     index=["Value1", "Value2", "Value3"]
# )
# print(s)
# print(type(s))
# print("================================================")
# print(df.surname)
# print(type(df.name))

print(df)


