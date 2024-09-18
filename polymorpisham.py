
# 1, method pverloading
# 2, method over riding
# 3, operator overloading


# method overriding

# class A:
#     def fun1(self):
#         print("base method")
        
# class B(A):
#     def fun1(self):
#         super().fun1()
#         print("Derived class")
        
# obj=B()
# obj.fun1()


# Operator overiding

class A:
    def fun1(self):
        self.a=int(input())
        self.b=int(input())
        
    def __add__(hello,hello2):
       print(hello.a,hello2.b)
       
obj1=A()
obj2=A()
obj1.fun1()
obj2.fun1()
obj1+obj2


