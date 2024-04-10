#recursive binary search

def rbs(a,n):
    print(a)
    start=0
    end=len(a)-1
    while start<end:
        mid=int((start+end)/2)
        if n==a[mid]:
            return 1
        elif n>a[mid]:
            start=mid+1
        elif n<a[mid]:
            end=mid-1
        else:
            return 0
        if start==end:
            if a[start]==n:
                return 1
            else:
                return 0

Array=[12,53,3,65,34,2,76,54,23,4]
Array.sort()
print(Array)
while True:
    tosearch=int(input("Enter the number you want to search "))

    ans=rbs(Array,tosearch)

    if ans==1:
        print(tosearch," is available in the list")
    else:
        print(tosearch," not available in the list")


    
