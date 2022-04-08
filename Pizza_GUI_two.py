from ast import Delete
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD



root = tk.Tk()

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

root.mainloop()