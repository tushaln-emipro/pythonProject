x = {'Key1','Key2','Key3'}
x.add('Key4')
print(x)

z = x.copy()
z.add('Key44')
print(z)
print(z.difference(x))

#print(x.pop())
#x.remove('Key1')
#print(x)

r = x.union(z)
print(r)