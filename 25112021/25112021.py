def fun(n):
    return lambda a: a * n


r = fun(3)
print('First Output of lambda with function')
print(r(3))

ages = [5, 12, 17, 18, 24, 32]
adults = filter(lambda a: False if (a <= 18) else True, ages)

print('Second Output of lambda with filter')
for x in adults:
    print(x)

adults1 = list(filter(lambda a: a >= 18, ages))
print('As list :', adults1)

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
finallist1 = list(map(lambda a: a * 3, _list))
finallist2 = list(map(lambda a: a * 3 if a > 5 else 0, _list))
finallist3 = list(filter(lambda a: a > 0, list(map(lambda a: a * 3 if a > 5 else 0, _list))))

print('Third Output of map with lambda,list')
print('Multiplication of each list values : ', finallist1)
print('Multiplication of each list values with if : ', finallist2)
print('remove 0 in list with filter : ', finallist3)

# reduce() with lambda()
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
_sum = reduce((lambda x, y: x + y), li)
print('get sum from list using reduce with lambda', _sum)

# using zip function
l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']
r = zip(l1, l2)
print('used zip fun', tuple(r))
