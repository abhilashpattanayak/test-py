class person :
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

 # Use the person class to create an object , and then execute the printname method :
class student(person):
    pass
x = student("mike", "olsen")
x.printname()           
