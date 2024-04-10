#input total no of sections and stream name in 11th class and display all info on the output

sections=0

class_11={}
instructions=("""Instructions to modify 
  1]  View the table.
  2]  Add stream to the table.
  3]  Remove a stream from the table.
  4]  Delete the table
  5]  View total no of sections.
  6]  Exit.  """)

print(instructions)
  
while True:

  work=input('Enter the number of the action you want to perform:  ')

  if '1' in work:
    if class_11=={}:
        print("Empty list")
    else:
        print(class_11)
  elif '2' in work:
    stream=input("Enter your stream name ")
    section=input("Enter the sectiton of the stream ")
    class_11[stream]=section
    sections+=1
    print("The stream ",stream ," has sucessfully been added to the table ")
    print(class_11)
  elif '3' in work:
    stream=input("Which stream do you want to remove : ")
    del(class_11[stream])
    sections-=1
    print("The ", stream ," has been sucessfully removed.")
    print(class_11)
  elif '4' in work:
    class_11.clear()
    sections=0
    print("Your shopping list has been emptied sucessfully ")
  elif '5' in work:
    print(sections)
  else:
      break
else:
  exit
