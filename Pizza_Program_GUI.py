import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Lists for each Pizza Menu
regularPizza = ["Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmetPizza = ["Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"]
variable = tk.StringVar()

#Combines both lists
reg_gour_pizza = regularPizza + gourmetPizza

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza")
Heading.grid(row = 0, column = 0, columnspan = 2)

#This widget creates a title for regular pizza
Regular_title = ttk.Label(root, text = "Regular pizza")
Regular_title.grid(row = 1, column = 0,)

#This widget creates a title for gourmet pizza
Gourmet_title = ttk.Label(root, text = "Gourmet pizza")
Gourmet_title.grid(row = 1, column = 1,)

#This widget creates the regular pizza menu
regular_menu = ttk.Label(root, text = "Hawaiian Pizza\nCheese Pizza\nBBQ Beef and Onion Pizza\nPepperoni Pizza\nCheezy Garlic Pizza\nVeggie lover Pizza\nHot and Spicy Veggie Pizza")
regular_menu.grid(row = 2, column = 0)

#This widget creates the gourmet pizza menu
regular_menu = ttk.Label(root, text = "Garlic Shrimp Pizza\nChicken Cranberry Pizza\nBuffalo Chicken Pizza\nMega Meat lovers Pizza\nMeat lovers Hot-dog stuffed Pizza")
regular_menu.grid(row = 2, column = 0)

#These widget's creates an OptionMenu for Dream Pizza
SelectPizza1 = ttk.OptionMenu(root, variable, text = reg_gour_pizza)
SelectPizza1.grid(row = 3, column = 0)

SelectPizza2 = ttk.OptionMenu(root, variable, text = reg_gour_pizza)
SelectPizza2.grid(row = 4, column = 0)

SelectPizza3 = ttk.OptionMenu(root, variable, text = reg_gour_pizza)
SelectPizza3.grid(row = 5, column = 0)

SelectPizza4 = ttk.OptionMenu(root, variable, text = reg_gour_pizza)
SelectPizza4.grid(row = 6, column = 0)

SelectPizza5 = ttk.OptionMenu(root, variable, text = reg_gour_pizza)
SelectPizza5.grid(row = 7, column = 0)

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

#Button widget to cancel order and 
cancelButton = ttk.Button(root, text = "Cancel Order")
cancelButton.grid(row = 8, column = 0)

#Button widget to go to next page
nextButton = ttk.Button(root, text = "Next")
nextButton.grid(row = 8, column = 1)

root.mainloop()