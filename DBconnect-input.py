import sys
import pymongo
import easygui

localhost=easygui.enterbox("Enter your localhost")
connection=pymongo.MongoClient(localhost)
db=connection.abc2
users=db.users

doc={'_id':'myid','firstname':'Terry','lastname':'cho'}

try:
    users.insert(doc)
except:
    choices=easygui.buttonbox("Your localhost is wrong",
                      choices=['back', 'quit'])
    if choices == "back":
        easygui.enterbox("Enter your localhost")

    else:
        easygui.msgbox("bye")
        
     

