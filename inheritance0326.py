##class A:
##    def hello(self):
##        self.name=input()
##
##class B:
##    def hello2(self): 
##        self.age=input()
##
##class C(B,A):
##    def hello3(self):
##        obj.hello()
##        obj.hello2()
##        print(obj.name,obj.age)
##obj=C()
##obj.hello3()


        ##multipule level inheritance
        
##class A:
##    def hello(self):
##        self.name=input()
##
##class B(A):
##    def hello2(self):
##        obj.hello()
##        self.location=input()
##
##class C(B):
##    def hello3(self):
##        obj.hello2()
##        print(obj.name,obj.location)
##
##obj=C()
##obj.hello3()
##
##


##class A:
##    def __init__(self):
##        self.age=10
##
##class B(A):
##    def hello(self):
##        self.age=20
##        print(self.age)
##
##class C(B):
##    def hello1(self):
##        print(self.age)
##
##obj=B()
##obj2=C()
##obj.hello()
##obj2.hello1()





class A:
    b=10
    def fun1(self):
        self.b=20
    def fun2(self):
        print(self.b,self.c)


obj1=A()
obj2=A()
A.b=100
obj1.fun1()
print(A.b)










