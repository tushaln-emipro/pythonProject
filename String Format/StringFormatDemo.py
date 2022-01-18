a = 'Hello  '
print(a)
print(a[1])

#for x in a:
#    print(x)

print("lll" in a)
print(a[1:2])

print(a.replace('H','T'))

age = 27
txt = "My name is Tushal, I am  " + str(age)
print(txt)

txt = "My name is Tushal, I am  {}"
print(txt.format(age))

#a = """this is
#        my log string"""
#print(a)

txt = 'this is my string of Stale'
print(txt.count('is'))
print(txt.capitalize())
print(txt.center(50))
_encode = txt.encode()
print(_encode)
_ew = txt.endswith('e')
print(_ew)
_fd = txt.find('my')
print(_fd)

txt = "Price is {price:.2f} dollars!"
print(txt.format(price = 10))

print(txt.index('is'))

txt = " "
x = txt.isspace()
print(x)

txt = "    this "
print(txt.lstrip())
txt = "12345"
_x = txt.rindex('2')
print(_x)

myTuble = ('x','y','z')
x = '#'.join(myTuble)
print(x)