#print a string backwards using recursive
while True:
    def revstr(ustr,first,end,ran):
        strlist=list(ustr)
        temp=strlist[first]
        strlist[first]=strlist[end]
        strlist[end]=temp
        first+=1
        end-=1
        if end==ran:
            print(str(strlist))
        else:
            revstr(strlist,first,end,ran)
    strinput=input("Enter your string ")
    length=len(strinput)
    run=int(length/2)
    run-=1
    revstr(strinput,0,length-1,run)
        
