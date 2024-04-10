user_input=input("how many cookies do you have ?")
user_cookies=int(user_input)
cookies_eaten=0
while user_cookies > 0 :
    user_cookies=user_cookies - 1
    cookies_eaten=cookies_eaten+1
    print ("Eating a cookie")
    print(cookies_eaten)
print ("I ate all the cookies.")
