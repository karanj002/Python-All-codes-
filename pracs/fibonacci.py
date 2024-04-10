#fibonacci series
import math

##def fib(n):
##    a=0
##    b=1
##    c=0
##    for i in range(0,n):
##        print(c,end=',')
##        c=a+b
##        a=b
##        b=c
##
##lim=int(input("Enter the limit of the series "))
##fib(lim)
##        
##def fibnorm(n):
##    if n <=1:
##        return n
##    else:
##        fn = ((1/math.sqrt(5))*((1+math.sqrt(5)/2)**n)) - ((1- math.sqrt(5))/2)** n)
##        
##
##fibnorm(10)


##n = 10
##fit = math.sqrt(5)
##fn = (1/fit)*(((1+fit/2)**n) - (((1- fit)/2)** n))
##print(fn)

n = 10
sqrtfive = math.sqrt(5)
alpha = (1+sqrtfive)/2
beta = (1-sqrtfive)/2
fn = (((alpha**n)-(beta**n))/(sqrtfive))

print(fn)

def fibBenit(n):
    fit = math.sqrt(5)
    a = ((1+fit)/2)**2
    b = ((1-fit)/2)**2
    
    ans = (a-b)/fit
    print(ans)

fibBenit(10)
