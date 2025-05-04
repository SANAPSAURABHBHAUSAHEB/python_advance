
class Employee:
    
    # No constructor overloading 
        
    def __init__(self, empid=1, ename="abc", salary=90000):
        self.empid=empid
        self.ename=ename
        self.salary=salary
    
    def printEmp(self):
        # empid=7
        print("EMPID:", self.empid)
        print("ENAME:", self.ename)
        print("SALARY:", self.salary)
        
    def bonusCalc(self):
        bonus = 0
        if self.salary < 100000:
            bonus = 200000
        self.salary += bonus
        print(f"new Salary after bonus: {self.salary}")
        
    def __repr__(self):
        return f"ENAME: {self.ename}, SALARY: {self.salary}"
        
    # @staticmethod #decorator:staticmethod deprecates performance
    # def hello():
    #     print("Hello world from class")
        

class Developer(Employee):
    
    def __init__(self, empid, ename, salary):
        super().__init__(empid, ename, salary)
        self.developerAllowannce = salary*0.05
    
    def writeCode(self):
        super().printEmp()
        print("Developer is writing code")
        
    def printEmp(self):
        super().printEmp()
        print("ALLOWANCE:", self.developerAllowannce)
        
    def __repr__(self):
        return f"{super().__repr__()}, ALLOWANCE: {self.developerAllowannce}"
        
        
    
    




e=Employee()
e.printEmp()
e.bonusCalc()

# Employee.hello()

e1=Employee(empid= 2, ename= "Ronak", salary= 9000)
e1.printEmp()
e1.bonusCalc()

d=Developer(empid= 3, ename= "Rohit", salary= 900000)
d.printEmp()
print(d)
