#swap
ulist=[1,2,3,4,5,6,7,8,9,0]

def swap(userlist):
    a=0
    b=1
    ran=int(len(userlist)/2)
    for i in range(0,ran):
        temp=userlist[a]
        userlist[a]=userlist[b]
        userlist[b]=temp
        a+=2
        b+=2
    return(userlist)

print(swap(ulist))
