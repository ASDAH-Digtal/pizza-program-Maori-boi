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
tk.title("Listbox")
listbox = tkinter.Listbox(tk)
listbox.pack()


text_box = tk.Text(root)
text_box.pack()

def button_click(entry):
    print('Entry:', entry.get())


for Pizza in regular_pizza:
    print(Pizza)

    entry = tk.Entry(text_box)
    entry.insert("end", Pizza)

    button = tk.Button(text_box, text = "Copy Variable", command = lambda x=entry:button_click(x))

    text_box.window_create(text_box.index("end"), window = button)
    text_box.window_create(text_box.index("end"), window = entry)
    
    text_box.insert("end", Pizza)
    text_box.insert("end", '\n')

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

    #Prints out Reciept of total order
result_label1 = ttk.Label(root, text = "$ ")
result_label1.grid(row = 1, column = 0, columnspan = 3)

#Customer Details if order is for delivery
Name = ttk.Entry(root)
Name.grid(row = 0, column = 1)

Address = ttk.Entry(root)
Address.grid(row = 1, column = 1)

PhoneNumber = ttk.Entry(root)
PhoneNumber.grid(row = 2, column = 1)

#Customer Details if order is for pick up
Name = ttk.Entry(root)
Name.grid(row = 0, column = 1)