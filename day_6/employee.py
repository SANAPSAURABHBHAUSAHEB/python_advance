class Employee:
    
    count = 0 # class variable
    
    def __init__(self, empid=1, ename="abc", basicSalary=90000):
        self.empid=empid
        self.ename=ename
        self.basicSalary=basicSalary
        self.hra=0.5*basicSalary
        self.pf=0.12*basicSalary
        self.pt=200
        self.__count1 = 0 # private variable
        
        Employee.count += 1   #class variable increment
        
    def calculateGross(self):
        return self.basicSalary + self.hra + self.pf + self.pt
    
    def calculateNetSalaries(self):
        return self.calculateGross() - self.pf - self.pt
    
    def __repr__(self):
        return f"EMPLOYEE[EMPID: {self.empid}, ENAME: {self.ename}, BASICSALARY: {self.basicSalary}, HRA: {self.hra}, PF: {self.pf}, PT: {self.pt}]"
    
    def __eq__(self, value):
        if self.calculateGross() == value.calculateGross():
            return True
        return False
    
    def __lt__(self, value):
        if self.calculateGross() < value.calculateGross():
            return True
        return False
    
    def __gt__(self, value):
        if self.calculateGross() > value.calculateGross():
            return True
        return False
        
class Manager(Employee):
    
    def __init__(self, empid=1, ename="abc", basicSalary=90000):
        super().__init__(empid, ename, basicSalary)
        self.foodAllowance=0.10*basicSalary
        self.managerAllowance=0.05*basicSalary
        self.otherAllowance=0.03*basicSalary
        
    def calculateGross(self):
        return super().calculateGross() + self.foodAllowance + self.managerAllowance + self.otherAllowance
        
    def __repr__(self):
        return f"MANAGER[{super().__repr__()}, FOODALLOWANCE: {self.foodAllowance}, MANAGERALLOWNACE: {self.managerAllowance}, OTHERALLOWANCE: {self.otherAllowance}]"
        
class MarketingExecutive(Employee):
    
    def __init__(self, empid=1, ename="abc", basicSalary=90000, distanceTravelled=10):
        super().__init__(empid, ename, basicSalary)
        self.phoneAllowance=1500
        self.kmRate = 100
        self.travelAllowance = distanceTravelled * self.kmRate
        
    def calculateGross(self):
        return super().calculateGross() + self.phoneAllowance + self.travelAllowance
        
    def __repr__(self):
        return f"MARKETINGEXECUTIVE[{super().__repr__()}, PHONEALLOWANCE: {self.phoneAllowance}, TRAVELALLOWANCE: {self.travelAllowance}]"
        
        
        
e=Employee()
print(e)
print(f"GROSS: {e.calculateGross()}")
print(f"NET: {e.calculateNetSalaries()}")

m=Manager()
print(m)
print(f"GROSS: {m.calculateGross()}")
print(f"NET: {m.calculateNetSalaries()}")

mexec=MarketingExecutive()
print(mexec)
print(f"GROSS: {mexec.calculateGross()}")
print(f"NET: {mexec.calculateNetSalaries()}")

objList = [e, m, mexec]

employeeList = []
managerList = []
marketingExecutiveList = []

for i in objList:
    if isinstance(i, Manager):
        managerList.append(i)
    elif isinstance(i, MarketingExecutive):
        marketingExecutiveList.append(i)
    elif isinstance(i, Employee):
        # print(i)
        employeeList.append(i)

print("Objs List ====>>>")
print(employeeList)
print(managerList)
print(marketingExecutiveList)

print(str(type(e)) == "<class '__main__.Employee'>")


# objectInitialValuesStr = input("Enter the Employee Details in Order empid , ename , basicSalary, employeetype ")

# objectInitialList = objectInitialValuesStr.split(",")


# if objectInitialList[3] == ""
# e1=Employee(objectInitialList[0], objectInitialList[1], int(objectInitialList[2]))
# print(e1)



e1=Employee(empid=8, ename="abc", basicSalary=2000)
print(e1)

e2=Employee(empid=1, ename="dabc", basicSalary=90000)
print(e2)

e3=Employee(empid=9, ename="wdabc", basicSalary=900000)
print(e2)

print(e1 == e2)
print(e1 > e2)
print(e1 < e2)

l = [e1, e2]
l.sort()
print(l)

# print(e2.__count1)
print(Employee.count)