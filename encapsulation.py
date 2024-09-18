 ## Encapsulation
 
#  1 Publlic - a=10
#  2 protect - _a=10
#  3 private - __a=10

 
# class Batch34():
    
#     def fun1(self):
#         self.a=10
#         self._b=20
#         self.__c=30
#     def fun2(self):
#         print(self.a,self._b,self.__c)
        
# class Batch33():
    
#     def fun3(self):
#         self.a=10
#         self._b=20
#         self.__c=30
#     def fun4(self):
#         print(self.a,self._b,self.__c)
        
        
# obj=Batch33()
# obj.fun1()
# obj.fun2()
# print(obj.a)
# print(obj._b)
# print(obj.__c)  #private vaiable ah access pandrathuku  print(obj._Batch34__c)

                                       ## MANGLIING METHOD
# class A:
#     def fun1(self):
#         print("public method")
#         # obj.__fun2()
        
#     def __fun2(self):
#         print("private method")
        
# obj=A()
# obj.fun1()
# obj._A__fun2() ## mangling method

class __A:
    def __fun2(self):
        self.__a= 10

obj=__A()
obj._A__fun2()