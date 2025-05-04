import pymysql
from pymysql.cursors import DictCursor
import pandas as pd

# create connection -- 
# host, port, user, password, 
# cursorclass: DictCursor (to get data in dictionary format)
connection = pymysql.connect(host='localhost', port=3306, user
='root', password='root', cursorclass=DictCursor)

# create cursor
mycursor = connection.cursor()

# use database
mycursor.execute("USE cdac")

# query all data from table employee
data = mycursor.execute("SELECT * FROM employee")
result = mycursor.fetchall()
print(result)

# get column names
# column_names = [desc[0] for desc in mycursor.description]
# print(mycursor.description)

# convert data to dataframe
# df = pd.DataFrame(result, columns=column_names)
df = pd.DataFrame(result)
print(df)

# cursor close
mycursor.close()

# connection close
connection.close()