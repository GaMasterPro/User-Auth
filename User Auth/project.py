import tkinter as tk
from tkinter import messagebox
import check_credentials
from check_credentials import adding_user, validatingEmail 

def style_entry(entry):
    entry.configure(bd=0, highlightthickness=0, relief=tk.FLAT, font=("Arial", 12))
    entry.configure(bg="#FFFFFF", fg="#333333")
    entry.configure(insertbackground='black')  

def open_signup_window():
    signup_window = tk.Toplevel(window)
    signup_window.geometry("400x300")
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="Sign Up", font=("Arial", 24, "bold")).pack(pady=10)
    tk.Label(signup_window, text="Username", font=("Arial", 15)).pack(pady=5)
    username_entry = tk.Entry(signup_window)
    username_entry.pack(pady=5)

    tk.Label(signup_window, text="Password", font=("Arial", 15)).pack(pady=5)
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.pack(pady=5)

    tk.Label(signup_window, text="Email", font=("Arial", 15)).pack(pady=5)
    email_entry = tk.Entry(signup_window)
    email_entry.pack(pady=5)

    signup_button = tk.Button(signup_window, text="Sign Up", font=("Arial", 15), command=lambda: signup(username_entry.get(), password_entry.get(), email_entry.get()))
    signup_button.pack(pady=10)

def signup(username, password, email):
    if not validatingEmail(email):
        messagebox.showwarning(message="Your email must contain '@'")
        return  

    if not username or not password:
        messagebox.showwarning(message="Username and password cannot be empty.")
        return 

    if adding_user(username, password, email):
        messagebox.showinfo(message="User was added successfully")
    else:
        messagebox.showerror(message="Username already exists or something went wrong")

def on_submit():
    username = email_entry.get()
    password = password_entry.get()

    if check_credentials.check_user_credentials(username, password):
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")


window = tk.Tk()
window.geometry("740x514")
window.title("Log in app")

canvas_top = tk.Canvas(window, width=740, height=55, highlightthickness=0)
canvas_top.pack(fill=tk.X)
canvas_top.create_rectangle(0, 0, 740, 55, fill="#FC5673", outline="")
canvas_top.create_text(370, 27.5, text="Welcome to our app", font=("Arial", 32, "bold"), fill="white")

canvas_main = tk.Canvas(window, width=740, height=514, highlightthickness=0, bg="#F5F5F5")
canvas_main.pack(fill=tk.BOTH, expand=True)

login_label = tk.Label(canvas_main, text="Log in", font=("Arial", 24, "bold"), fg="black", bg="#F5F5F5")
login_label.place(x=320, y=70)

email_label = tk.Label(canvas_main, text="UserName", font=("Arial", 15), fg="black", bg="#F5F5F5")
email_label.place(x=225, y=146)

password_label = tk.Label(canvas_main, text="Password", font=("Arial", 15), fg="black", bg="#F5F5F5")
password_label.place(x=225, y=230)

email_entry = tk.Entry(canvas_main)
style_entry(email_entry)
email_entry.place(x=249, y=195, width=241, height=32)

password_entry = tk.Entry(canvas_main, show="*")
style_entry(password_entry)
password_entry.place(x=249, y=265, width=241, height=32)

submit_button = tk.Button(canvas_main, text="Log in", font=("Arial", 15, "bold"), fg="#FFFFFF", bg="#FC5673", relief=tk.RAISED, bd=0, padx=20, pady=10, command=on_submit)
submit_button.place(x=316, y=310, width=108, height=36)

sign_up_button = tk.Button(canvas_main, text="Sign up", font=("Arial", 15, "bold"), fg="#FFFFFF", bg="#4CAF50", relief=tk.RAISED, bd=0, padx=20, pady=10, command=open_signup_window)
sign_up_button.place(x=316, y=360, width=108, height=36)

window.mainloop()
