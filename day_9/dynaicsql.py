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

