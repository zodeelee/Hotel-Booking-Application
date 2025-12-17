import tkinter as tk
from tkinter import messagebox
import pickle
import os

# storing user information via pickle db
data_file = "rooms.pickle"


class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Booking App")
        self.root.geometry("500x450")

        self.rooms = self.load_rooms()

        app_title = tk.Label(root, text="Hotel Booking App", font=("Arial", 18))
        app_title.pack(pady=15)

        # main 5 button widgets
        tk.Button(root, text="View Rooms",width=30, height=2,
                  command=self.view_rooms).pack(pady=8)

        tk.Button(root, text="Book Room",width=30, height=2,
                  command=self.book_room).pack(pady=8)

        tk.Button(root, text="Cancel Your Booking",width=30, height=2,
                  command=self.cancel_booking).pack(pady=8)

        tk.Button(root, text="View Your Booking",width=30, height=2,
                  command=self.view_bookings).pack(pady=8)

        tk.Button(root, text="Exit",width=30, height=2,command=root.quit).pack(pady=8)

    # -----------main button's menu--------------

    def view_rooms(self):
        text = "Select A Room To Book (101-105)\n"
        for room in self.rooms:
            if self.rooms[room] == "":
                text += f"[Single] Room {room}: Available\n"
            else:
                text += f"[Single] Room {room}: Booked\n"
        messagebox.showinfo("[Single] Room", text)

    def book_room(self):
        win = tk.Toplevel(self.root)
        win.title("Book Room")
        win.geometry("250x200")

        tk.Label(win, text="Room Number").pack()
        room_entry = tk.Entry(win)
        room_entry.pack()

        tk.Label(win, text="Your Name").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()

        def confirm():
            try:
                room = int(room_entry.get())
                name = name_entry.get()

                if room not in self.rooms:
                    messagebox.showerror("Error", "Room not found")
                    return

                if self.rooms[room] != "":
                    messagebox.showerror("Error", "Room already booked")
                    return

                self.rooms[room] = name
                self.save_rooms()
                messagebox.showinfo("Success", "Room booked!")
                win.destroy()

            except:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(win, text="Confirm", command=confirm).pack(pady=15)

    def cancel_booking(self):
        win = tk.Toplevel(self.root)
        win.title("Cancel Booking")
        win.geometry("250x150")

        tk.Label(win, text="Room Number").pack()
        room_entry = tk.Entry(win)
        room_entry.pack()

        def confirm():
            try:
                room = int(room_entry.get())

                if room not in self.rooms:
                    messagebox.showerror("Error", "Room not found")
                    return

                self.rooms[room] = ""
                self.save_rooms()
                messagebox.showinfo("Done", "Booking canceled")
                win.destroy()

            except:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(win, text="Cancel Booking", command=confirm).pack(pady=15)

    def view_bookings(self):
        text = ""
        for room in self.rooms:
            if self.rooms[room] != "":
                text += f"Room {room}: {self.rooms[room]}\n"

        if text == "":
            text = "No bookings yet."

        messagebox.showinfo("Bookings", text)

    # ------------pickle storing data -------------

    def save_rooms(self):
        f = open(data_file, "wb")
        pickle.dump(self.rooms, f)
        f.close()

    def load_rooms(self):
        if os.path.exists(data_file):
            f = open(data_file, "rb")
            data = pickle.load(f)
            f.close()
            return data

    # -------------5 rooms (101-105) -------------
        return {
            101: "",
            102: "",
            103: "",
            104: "",
            105: ""
        }


# ----------- Main Program -------------

root = tk.Tk()
app = HotelApp(root)
root.mainloop()