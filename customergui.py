from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Set up the main application window
root = Tk()
root.title("Customer Info Form")
root.geometry("400x500")

# --- Function to submit data to database ---
def submit_data():
    # Get data from entries
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    preferred = contact_method.get()

    # Check if name is filled out
    if name == "":
        messagebox.showwarning("Input Error", "Name field is required.")
        return

    # Save to database
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, birthday, email, phone, address, preferred_contact) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, birthday, email, phone, address, preferred))
    conn.commit()
    conn.close()

    # Clear fields
    name_entry.delete(0, END)
    birthday_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    contact_method.set("Email")

    messagebox.showinfo("Success", "Customer information saved.")

# --- Widgets ---

Label(root, text="Name").pack()
name_entry = Entry(root, width=40)
name_entry.pack()

Label(root, text="Birthday (YYYY-MM-DD)").pack()
birthday_entry = Entry(root, width=40)
birthday_entry.pack()

Label(root, text="Email").pack()
email_entry = Entry(root, width=40)
email_entry.pack()

Label(root, text="Phone").pack()
phone_entry = Entry(root, width=40)
phone_entry.pack()

Label(root, text="Address").pack()
address_entry = Entry(root, width=40)
address_entry.pack()

Label(root, text="Preferred Contact Method").pack()
contact_method = StringVar(value="Email")
Radiobutton(root, text="Email", variable=contact_method, value="Email").pack()
Radiobutton(root, text="Phone", variable=contact_method, value="Phone").pack()

Button(root, text="Submit", command=submit_data).pack(pady=20)

# Run the GUI loop
root.mainloop()
