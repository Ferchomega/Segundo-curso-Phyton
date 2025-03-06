a =1, 2, 3
print(type(a))
print(a[0])
a = (1,1,1,2,3,4)

print(a.count(1))
print(a.index(1))

a = set([1,2,3])
b = {3,4,5}
print(type(a))
print(type(b))
a.add(20)
print(a)
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
a.remove(20)
print(a)
print(dir(a))
