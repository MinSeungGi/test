from pymongo import MongoClient

conn = MongoClient('127.0.0.1')
print conn

employ = conn.test_db.collect
doc1 ={'empno':'1001'}
employ.insert(doc1)

result=employ.find()

for r in result:
    print r
