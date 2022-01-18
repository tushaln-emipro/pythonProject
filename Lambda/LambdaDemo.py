list = [{'a':10,'b':50},{'a':20,'b':10}]
list.sort(key=lambda i:i['a']);
print(list);

list.sort(key=lambda i:i['b']);
print(list);

x = lambda a : a + 10;
print(x(2))

x = lambda a,b : a + b;
print(x(2,2))

def myfun(n):
    return  lambda  a : a * n;

mydlr = myfun(2)
print(mydlr(11));

