#count all types of characters in a string

while True:
    letters=0
    digit=0
    space=0
    capital=0
    lower=0
    other=0
    string=input("Enter the string: ")
    
    for i in string:
        if i.isalpha():
            letters+=1
            if i.isupper():
                capital+=1
            if i.islower():
                lower+=1
        elif i.isspace():
            space+=1
        elif i.isnumeric():
            digit+=1
        else:
            other+=1
    print("no of alphabets= ",letters,"no of spaces=",space,"no of digits=",digit,capital,lower,other)
    
    
