import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

root = tk.Tk()

#Heading of the GUI
Heading = ttk.Label(root, text = "Dream Pizza", padding = 15, font = 10)
Heading.grid(row = 0, column = 0, columnspan = 2)

#Delivery Radiobutton
deliveryButton = ttk.Radiobutton(root, text = "Delvery")
deliveryButton.grid(row = 1, column = 0)

#Pick up Radiobutton
pickupButton = ttk.Radiobutton(root, text = "Pick up")
pickupButton.grid(row = 2, column = 0)

#Button widget to go to next page
nextButton = ttk.Button(root, text = "Next")
nextButton.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()