class Student:
    def __init__ (self,fn,ln):
        self.fname=fn
        self.lname=ln
    def SayHello(self):
        print("Hello " + self.fname + " " + self.lname)
        
    def GetFullNameInEthio(self):
        print("In Ethio  " + self.fname + " " + self.lname)
        
    def GetFullNameInWestern(self):
        print("In western  " + self.lname + " " + self.fname)
        
s1=Student("Nega","Tafere")
s1.GetFullNameInEthio()
s1.GetFullNameInWestern()

