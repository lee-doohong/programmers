from bisect import * 

a = [0, 1, 2]
b = a
c = a[:]
a[1] = 10

print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")