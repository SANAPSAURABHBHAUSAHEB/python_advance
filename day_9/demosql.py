import pymysql

connection = pymysql.connect(host='localhost', port=3306, user
='root', password='root')

mycursor = connection.cursor()

# Create a database
# mycursor.execute("CREATE DATABASE cdac")

# List all databases
# list_of_tables = mycursor.execute("SHOW DATABASES")
# print(list_of_tables)

mycursor.execute("USE cdac")

# Table creation
# mycursor.execute("CREATE TABLE employee (empid INT, ename VARCHAR(99), salary INT)")

# Insert data into table
# mycursor.execute("INSERT INTO employee VALUES (1, 'abc', 99000)")
# mycursor.execute("INSERT INTO employee VALUES (2, 'mnc', 98000)")
# mycursor.execute("INSERT INTO employee VALUES (3, 'dre', 95000)")

#query one rows
data = mycursor.execute("SELECT * FROM employee")
result1 = mycursor.fetchone()
result2 = mycursor.fetchone()
result3 = mycursor.fetchone()
result4 = mycursor.fetchone()
print(result1)
print(result2)
print(result3)
print(result4)

# query all rows
# data = mycursor.execute("SELECT * FROM employee")
# result = mycursor.fetchall()
# print(result)

# Delete a table
# mycursor.execute("DROP TABLE employee")

# Update the table
# connection.commit()

# cursor close
mycursor.close()

# connection close
connection.close()