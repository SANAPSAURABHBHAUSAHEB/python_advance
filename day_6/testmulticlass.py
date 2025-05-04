

class Employee:
    
    def __init__(self):
        self.id = 1
        
    def hello(self):
        print("hello employee")
        
class FinanaceManager(Employee):
    
    def hello(self):
        print("hello FinanaceManager")
    
class SalesManager(Employee):
    
    def hello(self):
        print("hello SalesManager")
        
class SalesFinance(FinanaceManager, SalesManager):
    
    def hello(self):
        SalesManager.hello(self)
        FinanaceManager.hello(self)
    
    # pass


e = Employee()
e.hello()

f = FinanaceManager()
f.hello()

s= SalesManager()
s.hello()

sf = SalesFinance()
sf.hello()