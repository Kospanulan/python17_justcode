# str1 = "apac"
# result = {
#     "a": 2,
#     "p": 1,
#     "c": 1
# }

result = {}
# print("1:", result)

result['key'] = 123
result[345] = 1
# print("2:", result)






str1 = "apac"
result = {}

for i in str1:
    if i in result:
        result[i] = result[i] + 1
    else:
        result[i] = 1


# for i in str1:
#     result[i] = result.get(i, 0) + 1


print(result)





