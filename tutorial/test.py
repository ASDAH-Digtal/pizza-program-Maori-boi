import tkinter as tk
from tkinter import ttk

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