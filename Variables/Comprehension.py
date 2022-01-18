listOne = [2,4,6];
listTwo = [2 * i for i in listOne if i > 2]
print(listTwo);

a = [1,2,3,4,5]
b = [i for i in a if i == 5]
print(b)

aa = [1,2,3,4,5]
bb = [i for i in a if i > 3]
print(bb)

# Receiving Tuples and Dictionaries in Functions
def sum(a,*args):
    total = 0
    for j in args:
        #total += pow(j,a)
        total += j + 2;
    return total

print(sum(2,10))

# The assert statement
myList = ['ab']
assert len(myList) >= 1
print(myList.pop())

