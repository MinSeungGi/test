numline =int(raw_input("How many line do you want?"))
k=0
for i in range(0,numline):
    for k in range(1,numline):
        print".",
        for j in range(1, numline):
            print "*"

        print
