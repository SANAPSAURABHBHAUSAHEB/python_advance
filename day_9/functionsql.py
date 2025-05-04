import pymysql

connection = pymysql.connect(host='localhost', port=3306, user
='root', password='root')

mycursor = connection.cursor()
mycursor.execute("USE cdac")
data = mycursor.execute("SELECT * FROM employee")
#create function to insert data into table
def insert(empid, ename, salary):
    mycursor.execute(f"INSERT INTO employee VALUES ({empid}, '{ename}', {salary})")
    connection.commit()

# function to update table

counter = 0
def update(empid, salary):
    # create new column to count no of times update operation is performed    
    mycursor.execute("SELECT counter FROM employee WHERE empid = %s", (empid,))
    result = mycursor.fetchone()
    if result:
        counter = result[0] + 1
    else:
        counter = 1
    
    # mycursor.execute(f"ALTER TABLE employee ADD COLUMN counter INT")
    # update counter column and salary column in one statement
    mycursor.execute(f"UPDATE employee SET counter = {counter}, salary = {salary} WHERE empid = {empid}")  
    connection.commit()
    
    
    
    

    
    
    # function to delete data from table
def delete(empid):
    mycursor.execute(f"DELETE FROM employee WHERE empid = {empid}")
    connection.commit()
    
    # function to display all data from table
def display():
    data = mycursor.execute("SELECT * FROM employee")
    
# insert (4, 'xyz', 100000)
# insert (5, 'pqr', 110000)

# update(1, 105000)
# delete(1)

# print(display())
# write function to take input from user and perform the operation
# counter function to count no of tmes update operation is performed

update(2, 550)


# cursor close
mycursor.close()

# connection close
connection.close()

class EmployeeDatabase:
    def __init__(self, host, port, user, password, database):
        self.connection = pymysql.connect(host=host, port=port, user=user, password=password)
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(f"USE {database}")

    def insert(self, empid, ename, salary):
        self.mycursor.execute(f"INSERT INTO employee VALUES ({empid}, '{ename}', {salary})")
        self.connection.commit()

    def update(self, empid, salary):
        self.mycursor.execute("SELECT counter FROM employee WHERE empid = %s", (empid,))
        result = self.mycursor.fetchone()
        counter = result[0] + 1 if result else 1
        self.mycursor.execute(f"UPDATE employee SET counter = {counter}, salary = {salary} WHERE empid = {empid}")
        self.connection.commit()

    def delete(self, empid):
        self.mycursor.execute(f"DELETE FROM employee WHERE empid = {empid}")
        self.connection.commit()

    def display(self):
        self.mycursor.execute("SELECT * FROM employee")
        return self.mycursor.fetchall()

    def close(self):
        self.mycursor.close()
        self.connection.close()


# Example usage:
db = EmployeeDatabase(host='localhost', port=3306, user='root', password='root', database='cdac')

# Perform operations
db.insert(4, 'xyz', 100000)
db.update(2, 550)
db.delete(1)
print(db.display())

# Close connection
db.close()