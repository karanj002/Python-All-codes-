#anagrams
letter=input("Enter your letter for anagram: ")
a=(letter)
print(a)
n=len(a)
print (n)
print(a[0])
for lett in range(0,n):
    for alph in range(a[lett],n):
        print(lett,alph)
