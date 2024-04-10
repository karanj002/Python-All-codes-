# This program calculates the square root of a number
user_response=input("Enter a number of which you want to know the square root of")
number=float(user_response)
guess=number/2
no_of_times=0
accuracy=0.01
while abs(number-(guess**2))>accuracy:
    print("Iteration ",no_of_times, "Guessed square root is ; ",guess)
    guess=(guess+(number/guess))/2
    no_of_times=no_of_times+1
print("Orignal number is ", number)
print("The square root of the number is ",guess)
