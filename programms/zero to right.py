#input a list of numbers
limit=int(input("Enter the no of elements the list : "))
listt=[]
for ele in range(0,limit):
    elem=int(input("Enter the list element : "))
    listt.append(elem)
print("The list items are ",listt)

for j in range(0,limit):
    for i in range(0,limit):
        if listt[j]==0:
            listt[j]=listt[i+1]
            listt[i+1]=0

print(listt)
    
