friends=[]
print "Enter 5 names:"
for i in range(5):
    friends.extend(raw_input())
num = int(raw_input("The names are 1,2,3,4,5, one name. which one? (1-5):"))
newname= raw_input("New name")
del friends[num]
friends.insert(num,newname)
print friends
