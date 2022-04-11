from ast import Delete
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

root = tk.Tk()

variable = tk.StringVar()
#Lists for each Pizza Menu
regularPizza = ["Select Pizza","Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmetPizza = ["Select Pizza","Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"] 

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza", padding = 15, font = 10)
Heading.grid(row = 0, column = 0, columnspan = 2)

#This widget creates a title for regular pizza
Regular_title = ttk.Label(root, text = "Regular pizza: $8.50", padding = 5, font = 5)
Regular_title.grid(row = 1, column = 0)

#This widget creates a title for gourmet pizza
Gourmet_title = ttk.Label(root, text = "Gourmet pizza: $13.50", padding = 5, font = 5)
Gourmet_title.grid(row = 1, column = 1)

#This widget creates the regular pizza menu
regular_menu = ttk.Label(root, text = "Hawaiian Pizza\nCheese Pizza\nBBQ Beef and Onion Pizza\nPepperoni Pizza\nCheezy Garlic Pizza\nVeggie lover Pizza\nHot and Spicy Veggie Pizza", padding = 10)
regular_menu.grid(row = 2, column = 0)

#This widget creates the gourmet pizza menu
regular_menu = ttk.Label(root, text = "Garlic Shrimp Pizza\nChicken Cranberry Pizza\nBuffalo Chicken Pizza\nMega Meat lovers Pizza\nMeat lovers Hot-dog stuffed Pizza", padding = 10)
regular_menu.grid(row = 2, column = 1)

#These widget's creates an OptionMenu for Dream Pizza
optionmenu1 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu1.grid(row = 3, column = 0)

optionmenu2 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu2.grid(row = 4, column = 0)

optionmenu3 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu3.grid(row = 5, column = 0)

optionmenu4 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu4.grid(row = 6, column = 0)

optionmenu5 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu5.grid(row = 7, column = 0)

#These widgets show the price of the pizza
price_pizza = ttk.Label(root, text = "$0.00")
price_pizza.grid(row = 3, column = 1)

price_pizza = ttk.Label(root, text = "$0.00")
price_pizza.grid(row = 4, column = 1)

price_pizza = ttk.Label(root, text = "$0.00")
price_pizza.grid(row = 5, column = 1)

price_pizza = ttk.Label(root, text = "$0.00")
price_pizza.grid(row = 6, column = 1)

price_pizza = ttk.Label(root, text = "$0.00")
price_pizza.grid(row = 7, column = 1)

#

#Heading for delivery
Heading = ttk.Label(root, text = "Dream Pizza Delivery or Pick up", padding = 15, font = 10)
Heading.grid(row = 8, column = 0, columnspan = 2)

#Delivery Radiobutton
deliveryButton = ttk.Radiobutton(root, text = "Delivery")
deliveryButton.grid(row = 9, column = 0, columnspan = 2)

#Pick up Radiobutton
pickupButton = ttk.Radiobutton(root, text = "Pick up")
pickupButton.grid(row = 10, column = 0, columnspan = 2)

Heading = ttk.Label(root, text = "Dream Pizza Delivery or Pick up", padding = 15, font = 10)
Heading.grid(row = 11, column = 0, columnspan = 2)

#Customer Details if order is for delivery
NameLabel = ttk.Label(root, text = "Name")
NameLabel.grid(row = 12, column = 0)

AddressLabel = ttk.Label(root, text = "Address")
AddressLabel.grid(row = 13, column = 0)

PhoneLabel = ttk.Label(root, text = "Phone Number")
PhoneLabel.grid(row = 14, column = 0)

#Customer Details if order is for delivery
Name_entry = ttk.Entry(root)
Name_entry.grid(row = 12, column = 1, columnspan = 2)


Address_entry = ttk.Entry(root)
Address_entry.grid(row = 13, column = 1, columnspan = 2)

PhoneNumber_entry = ttk.Entry(root)
PhoneNumber_entry.grid(row = 14, column = 1, columnspan = 2)

#Button widget to go to next page
cancelButton = ttk.Button(root, text = "Cancel Order")
cancelButton.grid(row = 18, column = 0)

#Button widget to go to next page
completeButton = ttk.Button(root, text = "Complete Order")
completeButton.grid(row = 18, column = 2)

#Button widget to go to next page
redoButton = ttk.Button(root, text = "Start Over")
redoButton.grid(row = 18, column = 4)

root.mainloop()