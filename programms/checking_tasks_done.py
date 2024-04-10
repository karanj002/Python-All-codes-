# A programme for checking the daily things to do

user_name= input("Enter your name ")
print("Hello "+ user_name + " let's check that have you completed your tasks for the day or not")
tasks_done_by_the_user=input("Have you completed all your tasks for today ?. if yes then write 'yes', if no then write 'no' .")
if "yes" in tasks_done_by_the_user :
    print("congrats you have bought yourself some time for the game time ")
else :
    print("you dumb ass cant you complete your tasks in time if you cant complete your tasks in time then just leave it ok. ")
print()
print("Well anyways now it's time for your daily checkup of tasks ")
print()
user_task1=input("Enter the first task of today ")
user_task2=input("Enter the second task of today")
user_task3=input("Enter the third task of today ")
user_task4=input("Enter the fourth task of today ")
user_checklist=(user_task1 , user_task2 , user_task3 , user_task4)
user_satisfaction=input("Is there any other task of today you want to check " )
if "yes" in user_satisfaction :
    print("Good to go then")
    if "1" in user_satisfaction :
        print("okie dokie" )
    user_task5=input("Enter the fifth task of today ")
elif "2" in user_satisfaction :
        print("ok fine ")
    user_task6=input("Enter the fsixth task of today ")
    user_task7=input("Enter the seventh task of today ")
    else :
        print("sorry bro its not programmed for so many tasks yet ")
else :
    print("You shithead how many more tasks have you thought of doing in a day ")




    
