hoursWorked = input("Enter hours worked this week: ")
n = int(hoursWorked)
ym = "YOU MADE"
dtw = "DOLLARS THIS WEEK"
if n < 0 or n > 168:
    print("INVALID")
elif n <= 40:
    n = n * 8
    print(ym,n,dtw)
elif 41 <= n <=50:
    n = n % 40 * 9 + 320 
    print(ym,n,dtw)
elif n >50:
    n = n % 50 * 10 + 420
    print(ym,n,dtw)
