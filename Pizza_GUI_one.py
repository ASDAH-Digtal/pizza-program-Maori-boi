import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Lists for each Pizza Menu
variable = tk.StringVar()
regularPizza = ["Select Pizza","Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"]
gourmetPizza = ["Select Pizza","Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"] 

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza Ordering System", padding = 15, font = 10)
Heading.grid(row = 0, column = 0, columnspan = 5)

#This widget creates a title for regular pizza
Regular_title = ttk.Label(root, text = "Regular pizza: $8.50", padding = 5, font = 5)
Regular_title.grid(row = 1, column = 1)
#This widget creates a title for gourmet pizza
Gourmet_title = ttk.Label(root, text = "Gourmet pizza: $13.50", padding = 5, font = 5)
Gourmet_title.grid(row = 1, column = 3)

#This widget creates the regular pizza menu
regular_menu = ttk.Label(root, text = "Hawaiian Pizza\nCheese Pizza\nBBQ Beef and Onion Pizza\nPepperoni Pizza\nCheezy Garlic Pizza\nVeggie lover Pizza\nHot and Spicy Veggie Pizza", padding = 10)
regular_menu.grid(row = 2, column = 1)
#This widget creates the gourmet pizza menu
Gourmet_menu = ttk.Label(root, text = "Garlic Shrimp Pizza\nChicken Cranberry Pizza\nBuffalo Chicken Pizza\nMega Meat lovers Pizza\nMeat lovers Hot-dog stuffed Pizza", padding = 10)
Gourmet_menu.grid(row = 2, column = 3)

#These widget's creates an OptionMenu for Dream Pizza
optionmenu1 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu1.grid(row = 3, column = 1)
optionmenu2 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu2.grid(row = 4, column = 1)
optionmenu3 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu3.grid(row = 5, column = 1)
optionmenu4 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu4.grid(row = 6, column = 1)
optionmenu5 = ttk.OptionMenu(root, variable, *regularPizza + gourmetPizza)
optionmenu5.grid(row = 7, column = 1)


#These widgets show the price of the pizza
price_pizza1 = ttk.Label(root, text = "$0.00", padding = 5)
price_pizza1.grid(row = 3, column = 3)
price_pizza2 = ttk.Label(root, text = "$0.00", padding = 5)
price_pizza2.grid(row = 4, column = 3)
price_pizza3 = ttk.Label(root, text = "$0.00", padding = 5)
price_pizza3.grid(row = 5, column = 3)
price_pizza4 = ttk.Label(root, text = "$0.00", padding = 5)
price_pizza4.grid(row = 6, column = 3)
price_pizza5 = ttk.Label(root, text = "$0.00", padding = 5)
price_pizza5.grid(row = 7, column = 3)

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza Ordering System: Customer Details", padding = 15, font = 10)
Heading.grid(row = 0, column = 0, columnspan = 5)

#Customer Details if order is for delivery
Name_Label = ttk.Label(root, text = "Name", padding = 5)
Name_Label.grid(row = 10, column = 1)
Address_Label = ttk.Label(root, text = "Address", padding = 5)
Address_Label.grid(row = 11, column = 1)
Phone_Label = ttk.Label(root, text = "Phone Number", padding = 5)
Name_Label = ttk.Label(root, text = "Name")
Name_Label.grid(row = 10, column = 1)
Address_Label = ttk.Label(root, text = "Address")
Address_Label.grid(row = 11, column = 1)
Phone_Label = ttk.Label(root, text = "Phone Number")
Phone_Label.grid(row = 12, column = 1)

#Customer enter's required information
Name_entry = ttk.Entry(root)
Name_entry.grid(row = 10, column = 3)
Address_entry = ttk.Entry(root)
Address_entry.grid(row = 11, column = 3)
Phone_entry = ttk.Entry(root)
Phone_entry.grid(row = 12, column = 3)

#Button widget to confirm customer details
confirmButton = ttk.Button(root, text = "Confirm Customer Details", padding = 5)
confirmButton.grid(row = 13, column = 2)

#Label widget to print customer details
nameLabel = ttk.Label(root, text = "Name: {}".format(Name_entry), padding = 5)
nameLabel.grid(row = 14, column = 2)
addressLabel = ttk.Label(root, text ="Address: {}".format(Address_entry), padding = 5)
addressLabel.grid(row = 15, column = 2)
phoneLabel = ttk.Label(root, text = "Phone Number: {}".format(Phone_entry), padding = 5)
phoneLabel.grid(row = 16, column = 2)

#Prints out Reciept of total order
result_label1 = ttk.Label(root, text = "Total cost: $0.00")
confirmButton = ttk.Button(root, text = "Confirm Customer Details")
confirmButton.grid(row = 13, column = 2)

#Label widget to print customer details
nameLabel = ttk.Label(root, text = "Name: {}".format(Name_entry))
nameLabel.grid(row = 14, column = 2)
addressLabel = ttk.Label(root, text ="Address: {}".format(Address_entry))
addressLabel.grid(row = 15, column = 2)
phoneLabel = ttk.Label(root, text = "Phone Number: {}".format(Phone_entry))
phoneLabel.grid(row = 16, column = 2)

#Prints out Reciept of total order
result_label1 = ttk.Label(root, text = "${}".format())
result_label1.grid(row = 17, column = 0, columnspan = 5)

#Button widget to cancel order and 
cancelButton = ttk.Button(root, text = "Cancel Order")
cancelButton.grid(row = 18, column = 0)
#Button widget to go to complete order
completeButton = ttk.Button(root, text = "Complete Order")
completeButton.grid(row = 18, column = 2)
#Button widget to restart order
restartButton = ttk.Button(root, text = "Restart Order")
restartButton.grid(row = 18, column = 4)

root.mainloop()