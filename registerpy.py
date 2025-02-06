import pyodbc # type: ignore
import tkinter as tk
from tkinter import messagebox
import hashlib
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

# SQL Server Connection Details
server = r'Servername'  # replace with your SQL Server name or IP address
database = 'registerpy'  # your database name
username = 'sa'  # your SQL Server username
password = 'password'  # your SQL Server password

# Create SQL Server connection
def connect_db():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              f'SERVER={server};'
                              f'DATABASE={database};'
                              f'UID={username};'
                              f'PWD={password}')
        return conn
    except pyodbc.Error as e:
        logging.error(f"Database connection error: {e}")
        messagebox.showerror("Database Error", "Failed to connect to the database.")
        return None

# Hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to insert the data into the database
def register_employee():
    emp_name = entry_name.get()
    emp_add = entry_address.get()
    emp_mobile = entry_mobile.get()
    emp_email = entry_email.get()
    emp_designation = entry_designation.get()
    emp_department = entry_department.get()
    user_id = entry_userid.get()
    password = entry_password.get()

    if not emp_name or not emp_mobile or not emp_email or not user_id or not password:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    hashed_password = hash_password(password)

    try:
        conn = connect_db()
        if conn is None:
            return
        cursor = conn.cursor()
        query = '''INSERT INTO Employee (EmpName, EmpAdd, EmpMobile, EmpEmail, Designation, Department, UserID, Password)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(query, (emp_name, emp_add, emp_mobile, emp_email, emp_designation, emp_department, user_id, hashed_password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Employee registered successfully!")
        clear_form()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Clear the form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_designation.delete(0, tk.END)
    entry_department.delete(0, tk.END)
    entry_userid.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Employee Registration Form")

# Create form labels and entry fields
tk.Label(root, text="Employee Name").grid(row=0, column=0, pady=10)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Employee Address").grid(row=1, column=0, pady=10)
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=1, column=1)

tk.Label(root, text="Mobile Number").grid(row=2, column=0, pady=10)
entry_mobile = tk.Entry(root, width=30)
entry_mobile.grid(row=2, column=1)

tk.Label(root, text="Email Address").grid(row=3, column=0, pady=10)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=3, column=1)

tk.Label(root, text="Designation").grid(row=4, column=0, pady=10)
entry_designation = tk.Entry(root, width=30)
entry_designation.grid(row=4, column=1)

tk.Label(root, text="Department").grid(row=5, column=0, pady=10)
entry_department = tk.Entry(root, width=30)
entry_department.grid(row=5, column=1)

tk.Label(root, text="User ID").grid(row=6, column=0, pady=10)
entry_userid = tk.Entry(root, width=30)
entry_userid.grid(row=6, column=1)

tk.Label(root, text="Password").grid(row=7, column=0, pady=10)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.grid(row=7, column=1)

# Register button
register_btn = tk.Button(root, text="Register", width=20, command=register_employee)
register_btn.grid(row=8, column=0, columnspan=2, pady=20)

root.mainloop()