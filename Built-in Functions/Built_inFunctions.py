#using map in function
def fun(n):
    return  len(n)
x = map(fun,('a','b1','c12'))
print(list(x))

def fun1(a,b):
    return a + b

x = map(fun1,('a','b1','c12'),('b','b2','c13'))
print(list(x))

#using filter in function
ages = [5,12,15,18,20,22,24,26]
def myfunc(x):
    if x < 18:
        return False
    else:
        return  True

adults = filter(myfunc,ages)
for x in adults:
    print(x)
    