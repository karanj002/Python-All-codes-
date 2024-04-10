#recur_fact(n)
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

def rec_fact(n):
    for i in n:
        print("Factorial of %d is "%i,fact(i))

ulist=[5,6,7,10]
rec_fact(ulist)
