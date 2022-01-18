#Python Inheritance

class ParentClass:
    def __init__(self,fn,ln):
        self.firstname = fn;
        self.lastname = ln;

    def printname(self):
        print(self.firstname,self.lastname);

x = ParentClass('T','N')
x.printname()

class ChildClass(ParentClass):
    def __init__(self,fn,ln,year):
        ParentClass.__init__(self,fn,ln);
        self.gy = year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.gy)

x = ChildClass('TUSHAL', 'NIMAVAT', 0)
x.printname()

z = ChildClass('TUSHAL','NIMAVAT',2021)
print(z.gy)
z.welcome()
