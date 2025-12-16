import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self):
        self.element = []






#==========Widgets===========
root = tk.Tk()
root.title("Hotel Booking application")
root.geometry("800x600")

#buttons
checkin_btn = tk.Button(root, text="check in", width=50, height=5)
checkin_btn.grid(row=0, column=1, padx=150, pady=150)

Room_select = tk.Button(root, text="select room", width 60, height=6)
Room_select.grid (row=0, column= 2, padx=150, pady=150)

name_id = tk.Button(root, text="select room", width 60, height=6)
name_id.grid (row=0, column= 3, padx=150, pady=150)

Phone_num = tk.Button(root, text="select room", width 60, height=6)
phone_num.grid (row=0, column= 4, padx=150, pady=150)

root.mainloop()

#Create a window
#root = tk.Tk()

# Add a label
#label = tk.Label(root, text="Hello, world!")
#label.pack()
