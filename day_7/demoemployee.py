class Employee:
    
    count = 0 # class variable
    
    def __init__(self, empid=1, ename="abc", basicSalary=90000):
        self.empid=empid
        self.ename=ename
        self.basicSalary=basicSalary
    
    def __repr__(self):
        return f"EMPLOYEE[EMPID: {self.empid}, ENAME: {self.ename}, BASICSALARY: {self.basicSalary}]"
    
    def __eq__(self, value):
        if self.basicSalary == value.basicSalary:
            return True
        return False
    
    def __lt__(self, value):
        if self.basicSalary < value.basicSalary:
            return True
        return False
    
    def __gt__(self, value):
        if self.basicSalary > value.basicSalary:
            return True
        return False
    
        
e1=Employee(empid=8, ename="abc", basicSalary=12000)
print(e1)

e2=Employee(empid=1, ename="dabc", basicSalary=8000)
print(e2)

e3=Employee(empid=9, ename="wdabc", basicSalary=900000)
e4 =Employee(empid=9,)
print(e2)

# print(e1 == e2)
print(e1 > e2)
print(e1 < e2)

l = [e1, e2,e3]
l.sort()
print(l)

# Sorting the list of employees by their basicSalary in descending order
# l.sort(key=lambda emp: emp.basicSalary, reverse=True)
l.sort(key=lambda emp: emp.basicSalary)
print(l)

# Filtering employees with basicSalary greater than 50000
filtered_employees = list(filter(lambda emp: emp.basicSalary > 50000, l))
print(filtered_employees)