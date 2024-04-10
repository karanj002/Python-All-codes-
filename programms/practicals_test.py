#factorial of a number
while True:
    limit=int(input("Enter the no. of  which you want to know the factorial of : "))
    p=1
    if limit>20:
        print("sorry software error ")
        break
    while limit>0:
        p=p*limit
        limit-=1
    print(p)

