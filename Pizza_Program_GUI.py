import tkinter as tk
from tkinter import ttk

root = tk.Tk()

variable = tk.StringVar()
regular_pizza = ["Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmet_pizza = ["Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"]


#This widget creates a Radiobutton
radiobutton = ttk.Radiobutton(root, text = "Option 1")
radiobutton.grid(row = 0, column = 1)

#This widget creates an OptionMenu
optionmenu = ttk.OptionMenu(root, variable, *regular_pizza + gourmet_pizza)
optionmenu.grid(row = 1, column = 0)

#This widget creates an Entry
entry = ttk.Entry(root)
entry.grid(row = 1, column = 1)

#This widget creates a text box/label
label = ttk.Label(root, text = regular_pizza)
label.grid(row = 2, column = 0, columnspan = 2)

#This widget creates a Button
button = ttk.Button(root, text = "Next",)
button.grid(row = 5, column = 0, columnspan = 2)

root.mainloop()