# Intro of the user

user_name=input('what is your name;')
if 'Stharanzn' in user_name :
    print("Hello sir we welcome you to your all in one python programme")
else :
    print ("Hello",user_name,".How are you doing, welcome to my All in one programme. Here I am programming whatever I have learnt in python language")
print()
print("First")

# Frist program (converting celsius into fahrenheit)

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
print()
print('Second')

# Finding the area and perimeter of the rectangle

print('here i am calculating the area and perimerter of the rectangle')

user_measurements=input ('Enter the length of the rectangle:')
user_measurement= input ('Enter the breadth of the rectangle:')
length= float ( user_measurements)
breadth= float ( user_measurement)
area= (length * breadth)
perimeter = 2 * ( length + breadth)

print ('The area of the rectangle is:',area)
print ( "The perimeter of the rectangle is:",perimeter)
print()
print('Third')

# Lists

print('I need to gather some information so please select the day today')
display=('Sunday(0)','Monday(1)','Tuesday(2)','Wednesday(3)','Thursday(4)','Friday(5)','Saturday(6)')
print ( display )
week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
usr_number=input ('Enter the day today by writing the days no. 0 - 6 : ')
usr_input=int (usr_number)
usr_day=(week_days[usr_input])
usr_date=input('What is the date today ? ')
usr_year=input('which year is it ? ')
usr_month=input('which month is it ? ')
print ('Oh so its',usr_day,'of',usr_date,'of',usr_month,'of',usr_year)
print()
print("Fourth")

# if else statements

print("Here i just need to know about your age .")
age_usr=input("What is your age ?")
age_user=int(age_usr)
if age_user<=12 :
    print("Hey you are still a kid yo")
elif age_user<=50:
    print("You are a matured person")
else :
    print("you are too old")
if 'allen' in user_name :
    print("par bsdk tu madarchod kab marega saale. Meri toh ek hi dua hai k tu saale jaldi marjaye bc")
elif 'Allen' in user_name :
    print("par bsdk tu madarchod kab marega saale. Meri toh ek hi dua hai k tu saale jaldi marjaye bc")
else :
    print("hope you live longer")
print()
print("fifth")
# Hours worked this week

print("Here I am calculating the money you would have earned for hours you worked in a week if you would have worked for me ;p")
hoursWorked=input("Enter the Hours you worked this week :")
n = int(hoursWorked)
ym = "YOU COULD HAVE MADE"
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

# This program calculates the square root of a number
print ( "In this program I am calculating the square root of your number")
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

#converting text into morse code

CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence

sentence = input("Enter sentence: ")
encodedSentence = convertToMorseCode(sentence)
print(encodedSentence)

def encodeToWords(sentence):
    encodedSentence = convertToMorseCode(sentence)
    for character in encodedSentence:
        if character == '-':
            print("Dash")
        elif character == '.':
            print("Dot")
        elif character == ' ':
            print('.')
        elif character == '_':
            print("Space")

sentence = input("Enter sentence: ")
encodeToWords(sentence)


    














