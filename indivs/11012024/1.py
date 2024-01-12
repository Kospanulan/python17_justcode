def get_count(x):
    result = {}

    for i in x:
        if i in result:
            result[i] = result[i] + 1
        else:
            result[i] = 1

    return result


def is_anogram(a,b):
    return get_count(a) == get_count(b)


str1 = "apa"
str2 = "paa"
if is_anogram(str1,str2):
    print("It's Anogram")
else:
    print("Isn't Anogram")