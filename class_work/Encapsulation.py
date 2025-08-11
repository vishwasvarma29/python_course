class Details:
    def __init__(self,name,mail,pwd):
        self.name=name
        self.mail=mail
        self.__pwd=pwd
    def getpassword(self):
        return self.__pwd
    def setpassword(self,new_password):
        self.__pwd=new_password
sumanth=Details("sumanth","sumanth@gmail.com","sumanth@123")
print(sumanth.name)
sumanth.name="sanjay"
print(sumanth.name)
print(sumanth.mail)
sumanth._mail="sanjay@gamil.com"
print(sumanth.mail)
print(getpassword(self))
print(setpassword(self,new_password):)

class Bank:
    def __init__(self):
        self.name="XYZ"
        self._balance=0
    @property
    def noresbalance(self):
        return self._balance
    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount
b=Bank()
print(b.noresbalance)
b.noresbalance=3000
print(b.noresbalance)
print(b.name)
b.name="abc"   
print(b.name)
