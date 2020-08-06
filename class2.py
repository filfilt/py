class Student:
    def __init__ (self,fn,ln):
        self.fname=fn
        self.lname=ln
    def SayHello(self):
        print("Hello " + self.fname + " " + self.lname)
s1=Student("Nega","Tafere")
s1.SayHello()
s2=Student("Alemu","Worku")
s2.SayHello()