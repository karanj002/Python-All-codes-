#queue

def push(val):
    myqueue.append(val)
    print(myqueue)

def pop():
    if len(myqueue)>0:
        myqueue.pop(0)
        print(myqueue)
    else:
        print(myqueue)
        print("Queue is empty")

myqueue=[]

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
