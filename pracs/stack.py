#stack

def push(val):
    mystack.append(val)
    print(mystack)

def pop():
    if len(mystack)>0:
        mystack.pop()
        print(mystack)
    else:
        print(mystack)
        print("stack is empty")

mystack=[]

while True:
    action=int(input("""
0 - pop
1-push
2-exit
"""))
    if action==0:
        pop()
    elif action==1:
        value=int(input("Enter the value to push "))
        push(value)
    else:
        break
