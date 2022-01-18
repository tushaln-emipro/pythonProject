list = [{'a':10,'b':50},{'a':20,'b':10}]
list.sort(key=lambda i:i['a']);
list.sort(key=lambda i:i['b']);
print(list);