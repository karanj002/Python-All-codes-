#perfect no
while True:
    no=int(input("Enter the no you want to check : " ))
    summ=0
    for series in range (1,no):
        if no%series ==0:
            digit=series
            summ+=digit

    if summ==no:
        print("it is a perfect no ")
    else:
        print("it is not a perfect no ")
