class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def  myfunc(self): 

      print ('Hello my name is ' + self.name) 

p1 =Person("jhon",35) 

p1.myfunc()
