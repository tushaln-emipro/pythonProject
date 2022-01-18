print("Hello World") # This is my print string

# Addition two values
a = 5; b = 10;
print(a+b);

# Subtraction tow values
a = 25; b = 5;
r = a - b;
print(r)

# Multiplication
a = 5; b  = 10;
r = a*b;
print(r);

# Divided
a = 100; b = 5;
r = a / b;
print(r);

def get_error_details():
    return (2, 'details')

errnum, errstr = get_error_details()

print(errnum)
print(errstr)

x = 1; y = 2;
print(x,y);

x,y = y,x;
print(x,y);

_str = 365;
print(str(_str));
print(len(str(_str)));

flag = False;
if flag: print(flag)

args = [['name','ilike','i']]
if args:
    if args[0][0] == 'name':
        # args[0] = ['|',('name','ilike',args[2])]
        print(args[0])