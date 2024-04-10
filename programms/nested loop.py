#nested loop
#loop within loop
user_limit=int(input("enter your limit"))
for i in range(1,user_limit+1):
    for j in range(1,user_limit+1):
        print(i,end='')
    print("_")
