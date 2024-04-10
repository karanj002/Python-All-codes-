#shopping list

shopping_list={}
print("""What do you want to do to your shopping list.. 
  1]  view your shopping list.
  2]  add item to your shopping list.
  3]  remove an item from your shopping list.
  4]  delete the shopping list.
  5]  Exit.  """)
  
while True:

  work=input('Enter the number of the action you want to perform:  ')

  if '1' in work:
    if shopping_list=={}:
        print("Empty list")
    else:
        print(shopping_list)
  elif '2' in work:
    item=input("Enter your item name ")
    quantity=int(input("Enter the quantity of the item "))
    if item in shopping_list:
      shopping_list[item]+=quantity
    else:
      shopping_list[item]=quantity
    print("The item ",item ," has been sucessfully been added to the list ")
    print(shopping_list)
  elif '3' in work:
    item=input("Which item do you want to remove : ")
    action=input("""Do you want to delete the whole item or specific amount
    [1] for whole item
    [2] for specific amount
    """)
    if "2" in action:
        quantity=int(input("Enter the amount to delete "))
        shopping_list[item]-=quantity
    else:
        del(shopping_list[item])
    print("The ", item ," has been sucessfully removed.")
    print(shopping_list)
  elif '4' in work:
    shopping_list.clear()
    print("Your shopping list has been emptied sucessfully ")
  else:
      break
else:
  exit
