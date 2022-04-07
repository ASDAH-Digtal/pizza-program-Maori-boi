import tkinter as tk
from tkinter import Label, ttk

root = tk.Tk()

variable = tk.StringVar()
ice_cream = ["Chocolate", "Strawberry", "Hokey Pokey", "Cookies and Cream", "Vegan"]

#This widget creates a Button
button = ttk.Button(root, text = "Button",)
button.grid(row = 0, column = 0)

#This widget creates a Radiobutton
radiobutton = ttk.Radiobutton(root, text = "Option 1")
radiobutton.grid(row = 0, column = 1)

#This widget creates an OptionMenu
optionmenu = ttk.OptionMenu(root, variable, *ice_cream)
optionmenu.grid(row = 1, column = 0)

#This widget creates an Entry
entry = ttk.Entry(root)
entry.grid(row = 1, column = 1)

#This widget creates a text box/label
label = ttk.Label(root, text = "Here is a random text")
label.grid(row = 2, column = 0, columnspan = 2)

root.mainloop()

import tkinter
tk = tkinter.Tk()

pizza = tk.IntVar()
pizza.set(1)

def calculate_pizza():

    pizza = int(Label.get()) 

    if(pizza==regular_pizza):
        print()
        result_pizza1 = pizza * 8.50

    elif(pizza==gourmet_pizza):
        print()
        result_pizza2 = pizza * 13.50

    result_label1.configure(text = "$".format(result_pizza1 + result_pizza2))

regular_pizza = ["Kai", "Cheese Pizza", "Cool Pizza"]
gourmet_pizza = ["Pai"]

    #Prints out Reciept of total order
result_label1 = ttk.Label(root, text = "$ ")
result_label1.grid(row = 1, column = 0, columnspan = 3)

#Customer Details if order is for delivery
Name_entry = ttk.Entry(root)
Name_entry.grid(row = 0, column = 1)

Address_entry = ttk.Entry(root)
Address_entry.grid(row = 1, column = 1)

PhoneNumber_entry = ttk.Entry(root)
PhoneNumber_entry.grid(row = 2, column = 1)

#Customer Details if order is for pick up
Name_entry = ttk.Entry(root)
Name_entry.grid(row = 0, column = 1)