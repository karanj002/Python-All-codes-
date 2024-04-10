# This program is to get the input (here celsius) nd convert it into fahrenheit
user_response=input ('Enter the temperature in celsius :')
celsius=float (user_response)
fahrenheit=( ( celsius*9) /5)+32
print ('The tempereture in fahrenheit is:',fahrenheit)
if fahrenheit<32 :
        print ("it is freezing ")
elif fahrenheit<50 :
        print("It is chilly")
elif fahrenheit< 90 :
        print("It is OK")
else :
        print("It is hot")

