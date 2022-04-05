import tkinter as tk
from tkinter import ttk

def calculate_pizza():

    pizza = int(entry.get()) 

    if(pizza==regular_pizza):
        print()
        result_pizza1 = pizza * 8.50

    elif(pizza==gourmet_pizza):
        print()
        result_pizza2 = pizza * 13.50

    result_label1.configure(text = "$".format(result_pizza1 + result_pizza2))

root = tk.Tk()

pizza = tk.IntVar()
pizza.set(1)

variable = tk.StringVar()
regular_pizza = ["Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmet_pizza = ["Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"]

Heading = ttk.Label(root, text = "Dream Pizza",)
Heading.grid(row = 0, column = 0, columnspan = 2)

#This widget creates an OptionMenu
optionmenu = ttk.OptionMenu(root, variable, *regular_pizza + gourmet_pizza)
optionmenu.grid(row = 1, column = 0)

#This widget creates an Entry
entry = ttk.Entry(root)
entry.grid(row = 1, column = 1)

#This widget creates a text box/label
RegularPizzaMenu = ttk.Label(root, text = regular_pizza)
RegularPizzaMenu.grid(row = 2, column = 0,)

GourmetPizzaMenu = ttk.Label(root, text = gourmet_pizza)
GourmetPizzaMenu.grid(row = 2, column = 1,)

#This widget creates a Button
button = ttk.Button(root, text = "Next",)
button.grid(row = 5, column = 0, columnspan = 2)


result_label1 = ttk.Label(root, text = "$ ")
result_label1.grid(row = 1, column = 0, columnspan = 3,)

root.mainloop()