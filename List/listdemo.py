list = [{'a':3,'b':5},{'a':2,'b':4},{'a':4,'b':10}]
list.sort(key=lambda i:i['a'])
print(list)

_r = 0;
for i in list:
    print(i['a'])

_r1 = [i for i in list if i['a'] > 2]
print(_r1)

Arry = ['a','b','c']
Arry.append('d')
print(Arry)
#print(Arry.clear())
ab = Arry.copy()
print(ab)

