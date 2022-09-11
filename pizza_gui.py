from tkinter import *
from tkinter import ttk

regularPizza = 8.50
gourmetPizza = 13.50

def update_cost():
    global regularPizza, gourmetPizza
    print()

root = Tk()
root.title("Dream Pizza Ordering Service")

gourmetPizza = StringVar()
gourmetPizza.set(["Garlic Shrimp Pizza", "Chicken Cranberry Pizza", "Buffalo Chicken Pizza", "Mega Meat lovers Pizza", "Meat lovers Hot-dog stuffed Pizza"]) 

regularPizza = StringVar()
regularPizza.set(["Hawaiian Pizza", "Cheese Pizza", "BBQ Beef and Onion Pizza", "Pepperoni Pizza", "Cheezy Garlic Pizza", "Veggie lover Pizza", "Hot and Spicy Veggie Pizza"])



#Heading of the GUI
top_frame = ttk.Label(root, text = "Dream Pizza Ordering System", font = 'ComicSansMS 12 bold')
top_frame.grid(row = 0, column = 0, columnspan = 5, padx = 50, pady = 25)

#This widget creates a title for regular pizza
Regular_title = ttk.Label(top_frame, text = "Regular pizza: $8.50", font = 'ComicSansMS 12 bold')
Regular_title.grid(row = 1, column = 1, padx = 25, pady = 12.5)
#This widget creates a title for gourmet pizza
Gourmet_title = ttk.Label(top_frame, text = "Gourmet pizza: $13.50", font = 'ComicSansMS 12 bold')
Gourmet_title.grid(row = 1, column = 3, padx = 25, pady = 12.5)

#This widget creates the regular pizza menu
regular_menu = ttk.Label(top_frame, text = "Hawaiian Pizza\nCheese Pizza\nBBQ Beef and Onion Pizza\nPepperoni Pizza\nCheezy Garlic Pizza\nVeggie lover Pizza\nHot and Spicy Veggie Pizza")
regular_menu.grid(row = 2, column = 1, padx = 12.5, pady = 6.25)
#This widget creates the gourmet pizza menu
Gourmet_menu = ttk.Label(top_frame, text = "Garlic Shrimp Pizza\nChicken Cranberry Pizza\nBuffalo Chicken Pizza\nMega Meat lovers Pizza\nMeat lovers Hot-dog stuffed Pizza")
Gourmet_menu.grid(row = 2, column = 3, padx = 12.5, pady = 6.25)

#These widget's creates an OptionMenu for Dream Pizza
optionmenu1 = ttk.OptionMenu(top_frame, variable, *regularPizza + gourmetPizza)
optionmenu1.grid(row = 3, column = 1)
optionmenu2 = ttk.OptionMenu(top_frame, variable, *regularPizza + gourmetPizza)
optionmenu2.grid(row = 4, column = 1)
optionmenu3 = ttk.OptionMenu(top_frame, variable, *regularPizza + gourmetPizza)
optionmenu3.grid(row = 5, column = 1)
optionmenu4 = ttk.OptionMenu(top_frame, variable, *regularPizza + gourmetPizza)
optionmenu4.grid(row = 6, column = 1)
optionmenu5 = ttk.OptionMenu(top_frame, variable, *regularPizza + gourmetPizza)
optionmenu5.grid(row = 7, column = 1)


#These widgets show the price of the pizza
price_pizza1 = ttk.Label(top_frame, text = "$0.00")
price_pizza1.grid(row = 3, column = 3)
price_pizza2 = ttk.Label(top_frame, text = "$0.00")
price_pizza2.grid(row = 4, column = 3)
price_pizza3 = ttk.Label(top_frame, text = "$0.00")
price_pizza3.grid(row = 5, column = 3)
price_pizza4 = ttk.Label(top_frame, text = "$0.00")
price_pizza4.grid(row = 6, column = 3)
price_pizza5 = ttk.Label(top_frame, text = "$0.00")
price_pizza5.grid(row = 7, column = 3)

#Heading of the GUI
bottom_frame = ttk.Label(root, text = "Dream Pizza Ordering System: Customer Details", font = 'ComicSansMS 12 bold')
bottom_frame.grid(row = 0, column = 0, columnspan = 5, padx = 50, pady = 25)

#Customer Details if order is for delivery
Name_Label = ttk.Label(bottom_frame, text = "Name")
Name_Label.grid(row = 0, column = 1)
Address_Label = ttk.Label(bottom_frame, text = "Address")
Address_Label.grid(row = 1, column = 1)
Phone_Label = ttk.Label(bottom_frame, text = "Phone Number")
Phone_Label.grid(row = 2, column = 1)

#Customer enter's required information
Name_entry = ttk.Entry(bottom_frame)
Name_entry.grid(row = 0, column = 3)
Address_entry = ttk.Entry(bottom_frame)
Address_entry.grid(row = 1, column = 3)
Phone_entry = ttk.Entry(bottom_frame)
Phone_entry.grid(row = 2, column = 3)

#Button widget to confirm customer details
confirmButton = ttk.Button(bottom_frame, text = "Confirm Customer Details")
confirmButton.grid(row = 3, column = 2)

#Label widget to print customer details
nameLabel = ttk.Label(bottom_frame, text = "Name: {}".format(Name_entry))
nameLabel.grid(row = 4, column = 2)
addressLabel = ttk.Label(bottom_frame, text ="Address: {}".format(Address_entry))
addressLabel.grid(row = 5, column = 2)
phoneLabel = ttk.Label(bottom_frame, text = "Phone Number: {}".format(Phone_entry))
phoneLabel.grid(row = 6, column = 2)

#Prints out Reciept of total order
result_label1 = ttk.Label(bottom_frame, text = "Total cost: $0.00")
result_label1.grid(row = 7, column = 0, columnspan = 5)


#Button widget to cancel order and 
cancelButton = ttk.Button(bottom_frame, text = "Cancel Order")
cancelButton.grid(row = 8, column = 1)
#Button widget to go to complete order
completeButton = ttk.Button(bottom_frame, text = "Complete Order")
completeButton.grid(row = 8, column = 2)
#Button widget to restart order
restartButton = ttk.Button(bottom_frame, text = "Restart Order")
restartButton.grid(row = 8, column = 3)

root.mainloop()