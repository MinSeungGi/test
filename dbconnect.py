import sys
import pymongo

connection=pymongo.MongoClient("mongodb://localhast")
db=connection.abc2
users=db.users

doc={'_id':'myid','firstname':'Terry','lastname':'cho'}

try:
    users.insert(doc)
except:
    print"insert failed",sys.exc_info()[0]