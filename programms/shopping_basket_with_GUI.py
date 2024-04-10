#shopping list

from tkinter import *
import tkinter as tk

screen=Tk()
screen.config(background="black")
screen.title("Shopping basket")
screen.geometry("520x360")
screen.resizable(0,0)

shopping_list={}
menu_label="""What do you want to do to your shopping list.. 
1]  view your shopping list.
2]  add item to your shopping list.
3]  remove an item from your shopping list.
4]  delete the shopping list.
5]  Exit.  """

Label(screen,text=menu_label,bg="black",fg="white",font="none 15 bold") .grid(row=0, column=1)

#definations
def view():
    output.delete(0.0,END)
    if shopping_list=={}:
        output.insert(END,"Your list is empty")
    else:
        output.insert(END,shopping_list)

def add():
    addwn=Tk()
    addwn.config(background="black")
    addwn.title("Add window")
    addwn.geometry("700x200")
    addwn.resizable(0,0)

    Label(addwn,text="Enter the item name",bg="black",fg="white",font="none 12 bold") .grid(row=0,column=0,sticky=W)
    item_entered=(Entry(addwn,width=20,bg="white"))
    item_entered.grid(row=0,column=1)

    Label(addwn,bg="black") .grid(row=1,column=0)

    Label(addwn,text="Enter the item quantity",bg="black",fg="white",font="none 12 bold") .grid(row=2,column=0,sticky=W)
    qty_entered=(Entry(addwn,width=20,bg="white"))
    qty_entered.grid(row=2,column=1)

    def add_to_list():
        try:
            add_item=item_entered.get().upper()
            add_qty=int(qty_entered.get())
            output.delete(0.0,END)
            if add_item in shopping_list:
                shopping_list[add_item]+=add_qty
            else:
                shopping_list[add_item]=add_qty
            output.insert(END,"Item added sucessfully")
        except:
            output.insert(END,"No quantity specified")

    Label(addwn,bg="black") .grid(row=3,column=0)
    Label(addwn,text="Status bar ===>",fg="white",bg="black",font="none 12 bold") .grid(row=4,column=0)
    output=Text(addwn,width=50,height=1,wrap=WORD,background="white")
    output.grid(row=4,column=1)
    
    Button(addwn,text="Add to the list ",width=10,command=add_to_list) .grid(row=1,column=2)
    output.delete(0.0,END)

def update():
    addwn=Tk()
    addwn.config(background="black")
    addwn.title("Add window")
    addwn.geometry("630x400")
    addwn.resizable(0,0)

    Label(addwn,text="For specific quantity",bg="black",fg="white",font="none 12 bold") .grid(row=0,column=1)

    Label(addwn,text="Enter the item name",bg="black",fg="white",font="none 12 bold") .grid(row=1,column=0,sticky=W)
    item_entered=(Entry(addwn,width=20,bg="white"))
    item_entered.grid(row=1,column=1)

    Label(addwn,bg="black") .grid(row=2,column=0)
    Label(addwn,bg="black") .grid(row=4,column=0)
    Label(addwn,bg="black") .grid(row=6,column=0)
    Label(addwn,bg="black") .grid(row=8,column=0)

    Label(addwn,text="Status bar ===>",fg="white",bg="black",font="none 12 bold") .grid(row=5,column=0)

    Label(addwn,text="Enter the item quantity",bg="black",fg="white",font="none 12 bold") .grid(row=3,column=0,sticky=W)
    qty_entered=(Entry(addwn,width=20,bg="white"))
    qty_entered.grid(row=3,column=1)

    def update_list():
        update_item=item_entered.get().upper()
        output.delete(0.0,END)
        try:
            if update_item in shopping_list:
                update_qty=int(qty_entered.get())
                shopping_list[update_item]-=update_qty
                output.insert(END,"item updated sucessfully")
                if shopping_list[update_item]<0:
                    output.delete(0.0,END)
                    del(shopping_list[update_item])
                    output.insert(END,"item deleted as the qty was 0")
            else:
                output.insert(END,"Item not found  ")
        except:
            if update_item=="":
                output.insert(END,"Item not entered  ")

    def delete_list():
        update_item=item_enteredd.get().upper()
        output.delete(0.0,END)
        try:
            del(shopping_list[update_item])
            output.insert(END,"item delelted sucessfully")
        except:
            output.insert(END,"No item specified")

    Button(addwn,text="""remove or update
    item from the list """,width=15,command=update_list) .grid(row=2,column=1,sticky=E)

    output=Text(addwn,width=50,height=1,wrap=WORD,background="white")
    output.grid(row=5,column=1)

    Label(addwn,text="For whole quantity",bg="black",fg="white",font="none 12 bold") .grid(row=7,column=1)

    Label(addwn,text="Enter the item name",bg="black",fg="white",font="none 12 bold") .grid(row=9,column=0,sticky=W)
    item_enteredd=(Entry(addwn,width=20,bg="white"))
    item_enteredd.grid(row=9,column=1,sticky=W)

    Button(addwn,text=" delete item ",width=15,command=delete_list) .grid(row=9,column=1)

def delete():
    addwn=Tk()
    addwn.config(background="black")
    addwn.geometry("300x50")
    addwn.resizable(0,0)

    Label(addwn,text="Are you sure to clear the shopping list",bg="black",fg="white",font="none 12 bold").grid(row=0,column=0)

    def yup():
        shopping_list.clear()
        addwn.destroy()

    def nope():
        addwn.destroy()

    v=tk.IntVar()
    rb1=Radiobutton(addwn,variable=v,value=1,text="Yes",command=yup) .grid(row=1,column=0,sticky=W)
    rb2=Radiobutton(addwn,variable=v,value=2,text="No",command=nope) .grid(row=1,column=0,sticky=E)

def exitt():
    screen.destroy()

v=tk.IntVar()
viewb=Radiobutton(screen,text="View",variable=v,value=1,command=view) .grid(row=1,column=1,sticky=W)
addb=Radiobutton(screen,text="Add",variable=v,value=2,command=add) .grid(row=1,column=1,sticky=E)
Label(screen,width=5,bg="black") .grid(row=2,column=0)
updateb=Radiobutton(screen,text="Update",variable=v,value=3,command=update) .grid(row=3,column=1,sticky=W)
deleteb=Radiobutton(screen,text="Delete",variable=v,value=4,command=delete) .grid(row=3,column=1,sticky=E)

Label(screen,bg="black").grid(row=1,column=0)
Label(screen,bg="black").grid(row=3,column=0)
Label(screen,bg="black").grid(row=6,column=0)

output=Text(screen,width=40,height=5,wrap=WORD,background="white")
output.grid(row=4,column=1)

exitb=Radiobutton(screen,text="Exit basket",variable=v,value=5,command=exitt) .grid(row=7,column=1)
