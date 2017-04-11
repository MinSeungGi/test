import sys
import pymongo

test = raw_input("Enter your localhost")
connection=pymongo.MongoClient(test)
db=connection.terrybd
users=db.users

doc={'testname':'min'}

try:
    users.insert(doc)
except:
    print"insert failed",sys.exc_info()[0]
     
