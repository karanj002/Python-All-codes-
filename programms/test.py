limit=int(input("Enter the no of elements the list : "))
listt=[]
for ele in range(0,limit):
    elem=int(input("Enter the list element : "))
    listt.append(elem)
print("The list items are ",listt)

for i in range(0, limit):
    for j in range(0, i):
        if listt[i]<0 and listt[j]>0:
            temp=listt[j]
            listt[j]=listt[i]
            listt[i]=temp
            print(listt)
