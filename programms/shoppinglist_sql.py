#shopping list
import mysql.connector as myc
import pickle
import platform

requireddatabase = 'shopping_data'
conn = None
menu = """##############################################################################################
                    What do you want to do to your shopping list.. 
                    1]  View your shopping list.
                    2]  Add item to your shopping list.
                    3]  Remove an item from your shopping list.
                    4]  Clear the shopping list.
                    5]  Exit.
##############################################################################################
\n >>>"""

def proceed(conn):
  global requireddatabase
  cursor = conn.cursor()
  cursor.execute("show databases")
  databases = cursor.fetchall()

  for i in range(len(databases)):
    if databases[i][0] == requireddatabase:
      cursor.execute("use " + requireddatabase )
      dataexists = True
      break
      
    else:
      dataexists = False

  if dataexists == False:
    cursor.execute("create database " + requireddatabase)
    cursor.execute("use " + requireddatabase)
    cursor.execute("create table shopping_list (Item varchar(20), Qty int, primary key(Item))")
    
  return cursor

#to convert tupled list to normal list
def purifylist(topurify):
  templist = []
  for i in range(len(topurify)):
    templist.append(topurify[i][0])
  return templist

def gettables(cursor):
  cursor.execute("select item from shopping_list")
  tables = cursor.fetchall()

  return purifylist(tables)

#option 1
def viewtable(cursor):
  if gettables(cursor) == []:
    print("The shopping list is empty\n")

  else:
    cursor.execute("select * from shopping_list")
    items_list = cursor.fetchall()
    for i in range(len(items_list)):
      print(f" {items_list[i][0]} {items_list[i][1]} Kgs   ")
      
#option 2
def insert(cursor,item,qty):
  global conn
  if item not in gettables(cursor):
    sqlcode = f"insert into shopping_list values( '{item}' , {qty})"
    cursor.execute(sqlcode )
    print(f"\n{item} added susessfully \n")
    
  else:
    while True:
      do = input(f"{item} already exists in the table, would you like to update its quantity? (y,n)\n")
      do = do.strip()
      do.lower()
      
      if do == 'y':
        removeqty(cursor,item,int(qty))
        break
      
      elif do == 'n':
        print(f'Dropping action to add {item}\n')
        break
      
      else:
        print("Please enter either y or n")
  viewtable(cursor)
  conn.commit()

#option 3 (1)
def removeitem(cursor,item):
  global conn
  cursor.execute("select item from shopping_list")
  items = cursor.fetchall()
  purifieditems = purifylist(items)
  
  if item not in purifieditems:
    print(f"{item} does not exist in the table")

  else:
    cursor.execute(f"delete from shopping_list where item = '{item}'")
    print(f"\n{item} removed susessfully \n")
  conn.commit()

#Establishing connection
def connect():
  global conn
  trustdevice = 0
  udata = []
  try:
    udata = pickle.load('udata.box','rb')
    if udata[0] == 'trust':
      trustdevice = 1
    else:
      trustdevice = 0
  except:
    pass
  while True:
    try:
      if trustdevice == 0:
        upass = input("Enter password for your mysql database (user: root) \n")
        conn= myc.connect(host = 'localhost', user = 'root', passwd = upass)
        return proceed(conn)
        break
      else:
        conn= myc.connect(host = 'localhost', user = 'root', passwd = udata[1])
    
    except Exception as e:
      print(e)

#option 3 (2)
def removeqty(cursor,item,qty):
  if qty >0:
    cursor.execute(f"update shopping_list set qty = {qty} where item = '{item}'")
    
  else:
    cursor.execute(f"delete from shopping_list where item = '{item}'")

#option 4 
def clear(cursor):
  global conn
  while True:
    sure = input("Would you like to clear the shopping_list (y,n):\n")
    sure = sure.strip()
    sure = sure.lower()
    
    if sure == 'y':
      cursor.execute('truncate table shopping_list')
      print("Data cleared successfully \nYour list is now empty")
      break
    
    elif sure == 'n':
      break
    
    else:
      print('Please enter a valid input ')
  conn.commit()
      

def main():
  
  finalcursor = connect()
  
  while True:
    while True:
      try:
        todo = int(input(menu))
        break
      
      except:
        print("Please Enter a valid input \n")

    if todo == 1:
      viewtable(finalcursor)
    
    elif todo == 2:
      itemname = input("Enter item name \n")
      itemname = itemname.strip()
      itemname = itemname.upper()
      while True:
        try:
          itemqty = int(input("Enter the quantity (in kgs) \n"))
          break
        
        except:
          print('please enter a valid quantity \n')
      insert(finalcursor,itemname,itemqty)

    elif todo == 3:
      while True:
        try:
          delaction = int(input("would like to \n1) Remove the whole item  \n2) Update its quantity \n"))
          break
        
        except:
          print("Please enter a valid option\n")
      if delaction == 1:
        itemname = input("Enter the item name you want to delete \n")
        itemname = itemname.strip()
        itemname = itemname.upper()
        removeitem(finalcursor,itemname)

      elif delaction == 2:
        itemname = input("Enter the item name you want to update \n")
        itemname = itemname.strip()
        itemname = itemname.upper()
        while True:
          try:
            itemqty = int(input("Enter the quantity to update(in kgs) \n"))
            break
          
          except:
            print("Please enter a valid quantity to delete")
        removeqty(finalcursor,itemname,itemqty)

    elif todo == 4:
      clear(finalcursor)
        
    elif todo == 5:
      conn.commit()
      print("Good bye :)")
      break

    else:
      print("Please enter a valid option")
      
      

main()
