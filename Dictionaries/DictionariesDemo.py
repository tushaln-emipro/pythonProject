_dict = {'Name':'Tushal','City':'Rajkot','State':'GJ','Status':True,'Other':['a','b']}
print(_dict)
print(_dict['Name'])
print(len(_dict))

x = ('Key1','Key2','Key3')
y = 5
z = dict.fromkeys(x,y)
print(z)

#print(_dict.get('Name'))
#print(_dict.items())
#print(_dict.values())

flist = ['a','b','c']
flist.insert(3,'d')
print(flist)

flist.pop(1)
print(flist)

x = flist.copy()
print(x)

for j in x:
    print(j)

for jj in _dict:
    print(_dict[jj])

for x in _dict.values():
    print(x)

for x,y  in _dict.items():
    print(x,y)