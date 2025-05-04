import pymongo

db = pymongo.MongoClient('mongodb://localhost:27017/')
# print(db.list_database_names())
mydb = db["demo"]
# x = mydb.list_collection_names()
# print(x)
mytable = mydb["employee"]
# a = {"empid": 1, "ename": "abc", "salary": 99000}
# print(mytable.insert_one(a))
data = mytable.find()


# write class to perform CRUD operation on mongo db
# insert, update, delete, display

# Example usage:
class dboperations:
    def __init__(self, host, port, user, password, database):
        self.connection = pymongo.MongoClient(host, port)
        self.mydb = self.connection[database]
        self.mytable = self.mydb["employee"]
    
    def insert(self, empid, ename, salary):
        a = {"empid": empid, "ename": ename, "salary": salary}
        self.mytable.insert_one(a)
    
    def update(self, empid, salary):
        self.mytable.update_one({"empid": empid}, {"$set": {"salary": salary}})
    
    def delete(self, empid):
        self.mytable.delete_one({"empid": empid})
    
    def display(self):
        data = self.mytable.find()
        for i in data:
            print(i)
    
    def close(self):
        self.connection.close()
#use file io operation
# how to pass parameter as file while connecting mongodb in python

db = dboperations('localhost', 27017, 'root', 'root', 'demo')
# 
# db.insert(3, 'dre', 95000) 
# db.insert(4, 'xyz', 10000)
# db.delete(3) 
# db.delete(4)
# upsert: True
# db.update(3,550)
# db.display()
# upsert: True
# db.update(3,550)
# db.display()

# upsert: True
# db.update(1000,550)

db.close()
    
    
    
 