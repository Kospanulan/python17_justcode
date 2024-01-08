
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s1 = {1, 3, 5, 7}
# s2 = {2, 4, 6, 8}
# s3 = {1, 3, 5, 7, 9}

a = {1, 3, 5, 9}
b = {2, 4, 5, 9}
c = {5, 9}

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}\n")

res_u = a.union(b)
print(f"union: {res_u}")

res_i = a.intersection(b)
print(f"intersection: {res_i}")

res_dif1 = a.difference(b)
# a = a.difference(b)
# a.difference_update(b)
# print(f"\na: {a}\n")

print(f"difference a - b: {res_dif1}")
print(f"difference a - b v2: {a - b}")

res_dif2 = b.difference(a)
print(f"difference b - a: {res_dif2}")
print(f"difference b - a v2: {b - a}")

res_sym_dif = a.symmetric_difference(b)
print(f"sym difference: {res_sym_dif}")


res1 = c.issubset(a)
print(f"c issubset a: {res1}")
res2 = a.issuperset(c)
print(f"a issuperset c: {res2}")

# a.clear()
# print(f"new a: {a}")

