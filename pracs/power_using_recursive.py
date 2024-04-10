#calc a**b
while True:
    def calc(a,b,z):
        c=a**z
        z+=1
        b-=1
        if b==0:
            print(c)
        else:
            calc(a,b,z)
        

    number=int(input("Enter the number "))
    power=int(input("Enter the power "))
    calc(number,power,1)
