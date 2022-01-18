#How to define a functions
def my_fun():
    print('This my first fun')

my_fun()

def my_funParam(name):
    print(name + ' ref')

my_funParam('a')

def myfun2param(a,b):
    r = a + b
    return  print(r)
myfun2param(5,2)

def myArrayfun(*arry):
    print('Position ' + arry[1])

myArrayfun('1','2','3')

def myunknownfun(**param):
    print('His last name is ' + param['ln'])

myunknownfun(fn= 'T',ln = 'N')

def myloopfun(list,p):
    for i in list:
        if i == 2:
            print(i)

list = [1,2,3]
myloopfun(list,2)

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('recursion fun')
tri_recursion(4)

#Call one function from another

def MainFun(x):
    return  (x * x)

def Child1fun(Arry,n):
    sum = 0
    for i in range(n):
        sv = MainFun(Arry[i])
        sum += sv
    return  sum

Array = [1,2,3,4,5,6,7,8,9,10]
n = len(Array)
total = Child1fun(Array,n)
print('Sum of the Squere of list of Number : ',total)

#how to return value from one function

def return_55():
    return 55

num = return_55()
print(num)