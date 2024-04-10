def palin(s):
    if len(s)<2:
        return True
    else:
        if s[0]==s[-1]:
            s.pop(0)
            s.pop()
            return palin(s)
        else:
            return False
while True:
    strin=input("Enter a word")
    strin=strin.upper()
    stri=list(strin)

    if (palin(stri)==True):
        print("yup")
    else:
        print("nope")
