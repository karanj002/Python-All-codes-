#try and except
table=[]
while True:
    user_name=input("Enter your name :- ")
    user_age=int(input("Enter your no :- "))
    table.append(user_age)
    if user_age in table:
        try:
            print("This no is already taken.")
            user_age=int(input("Enter your new no :- "))
        except :
            print("This no is now taken.")

        
