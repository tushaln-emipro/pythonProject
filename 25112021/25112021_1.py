# List Comprehension
citylist = ['rajkot', 'surat', 'pune']
newlist = []


for i in citylist:
    if 'a' in i:
        newlist.append(i)


print('using for with if')
print(newlist)

newlist = list(filter(lambda a1: 'a' in a1, citylist))
print('using list,filter,lambda')
print(newlist)

newlist = [x for x in citylist if 'a' in x]
print('using for,if')
print(newlist)
newlist = [x if x != 'pune' else 'MH' for x in citylist]
print(newlist)

newlist = [x if x != 'pune' else 'MH' for x in citylist]
newlist.sort()
print('using for,if,sort')
print(newlist)

numlist = [25, 20, 10, 5, 1]
numlist.sort(reverse=False)
print('using sort,reverse')
print(numlist)

numlist.sort(key=(lambda aa: abs(aa - 50)))
print('using sort,abs')
print(numlist)

# Join Two Lists
lt1 = ['a', 'b', 'c']
lt2 = ['d', 'e', 'f']
lt3 = lt1 + lt2
print('Join Two Lists 1 ', lt3)

for a in lt2:
    lt1.append(a)
print('Join Two Lists 2 ', lt1)

lt1.extend(lt2)
print('Join Two Lists 3 ', lt1)
