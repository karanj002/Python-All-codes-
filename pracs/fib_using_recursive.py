#fibonacci series using recursive
import math

def fibrecurve(n,a,b):
    if a == 0 and b == 1:
        print('0,1',end = ',')
    c=a+b
    print(c,end=",")
    n-=1
    a=b
    b=c
    if n==0:
        pass
    else:
        fibrecurve(n,a,b)
        

def fib(n):
    if n ==1:
        return 1
    elif n == 2 :
        return 2
    else:
        c = fib(n-1) + fib(n-2)
        return c

def fibstart(x):   
    for i in range(x+1):
        if i == 0:
            pass
        elif i == 1:
            print('0,1,1',end = ',')
        else:
            print(fib(i),end = ',')

def fibBenit(n):
    for i in range(n+2):
        fit = math.sqrt(5)
        a = (1+fit)/2
        b = (1-fit)/2
        fn = int((((a**i)-(b**i))/(fit)))
        
        print(fn,end = ',')
        

while True:
    choose = int(input("\nEnter which method to use to find the fibonacci series\n \t1).Recursive method\n \t2).Benedict method\n \t99).Exit\n"))

    if choose == 99:
        break
    else:
        lim = int(input("\nEnter the limit for the series\n"))
        
    if choose == 1:
        print("\nCustom method\n")
        fibrecurve(lim,0,1)
        print("\nTaught method\n")
        fibstart(lim)
        

    elif choose == 2:
        fibBenit(lim)

    else:
        print('\nPlease enter a valid option \n')
        
