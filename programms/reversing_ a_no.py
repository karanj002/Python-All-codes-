# reversing a number
ui=int(input("enter a number to reverse it "))
d=0
r=0
while ui >1:
    d=d*10
    r=int(ui%10)
    ui=ui/10
    d=d+r
print(d)
