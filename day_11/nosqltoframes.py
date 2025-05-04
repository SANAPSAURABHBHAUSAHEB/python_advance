import pandas as pd 
from pymongo import MongoClient

# create connection
# host, port, user, password
db = MongoClient('mongodb://localhost:27017/')

# get database
mydb = db["demo"]

# get collection
mytable = mydb["employee"]

# query all documents from collection
data = mytable.find()
data = list(data)

# print queried data
print(data)

# convert data to dataframe
df = pd.DataFrame(list(data))
print(df)

# close connection
db.close()