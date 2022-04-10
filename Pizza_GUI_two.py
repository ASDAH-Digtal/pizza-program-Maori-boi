import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

root = tk.Tk()

variable = tk.StringVar
regularPizza = ["Select Pizza","Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmetPizza = ["Select Pizza","Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"] 

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza", padding = 15, font = 10)
Heading.grid(row = 0, column = 0)

deliveryButton = ttk.Radiobutton(root, text = "Delvery")
deliveryButton.grid(row = 1, column = 0)

pickupButton = ttk.Radiobutton(root, text = "Pick up")
pickupButton.grid(row = 2, column = 0)

#Prints out Reciept of total order
result_label1 = ttk.Label(root, text = "$ ")
result_label1.grid(row = 1, column = 0)
root.mainloop()