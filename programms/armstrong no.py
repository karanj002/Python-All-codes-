#check for armstrong no.
#armstrong no is a 3 digit no whose sum of cube of every no is equal to the no.
#eg . 371
#3**3+7**3+1**3=371
while True:
    check=int(input("Enter the no you want to check :"))

    summ=0
    temp=check
    while temp>0:
        digit=temp% 10
        summ +=digit **3
        temp //=10

    if check ==summ:
        print(check, "is an armstrong no")
    else:
        print(check,"is not an armstrong no")

