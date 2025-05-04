

class Employee:
    
    def __init__(self, id =1, salary=10000):
        self.id = id
        self.salary = salary
        
    def hello(self):
        print("hello employee")
        
    def __repr__(self):
        return f"EMPLOYEE [ ID: {self.id}, SALARY: {self.salary}]"
    
    def __eq__(self, value):
        if self.id == value.id:
            return True
        return False
    
    def __gt__(self, other):
        if self.id > other.id:
            return True
        return False
    
    def __lt__(self, other):
        if self.id < other.id:
            return True
        return False
    
    def __add__(self, other):
        return self.id + other.id
    
    # def __sort__(self, other):
    #     if self.salary > other.salary:
    #         return self.salary
    #     return other.salary
    
    
e1 = Employee(id=8)
print(e1)

e2 = Employee(id=1)
print(e2)

# print(e1 == e2)
print(e1 > e2)
print(e1 < e2)
print(e1 + e2)

l = [e1, e2]
print(l)
l.sort()
print(l)