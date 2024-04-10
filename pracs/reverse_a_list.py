#reversing a list
ulist=list(input("Enter your list elements "))
def rever(userlist):
    first=0
    end=len(userlist)-1
    ran=int(len(userlist)/2)
    for i in range(0,ran):
        temp=userlist[i]
        userlist[i]=userlist[end]
        userlist[end]=temp
        end-=1
    return userlist

print(rever(ulist))
    
