
import tkinter as tk
import sqlite3
from tkinter import messagebox
import tkinter.font as font
# https://www.youtube.com/watch?v=QfhF9BnmN6E



def login():
    app = sqlite3.connect('login.db')
    app.execute('CREATE TABLE IF NOT EXISTS login(username TEXT NOT NULL,password TEXT NOT NULL)')
    # app.execute('INSERT INTO login(username, password) VALUES("admin", "admin")')
    app.execute('INSERT INTO login(username, password) VALUES("user", "admin")')

    cursor = app.cursor()
    cursor.execute('SELECT * FROM login where username=? AND password=?',(user_input.get(), password_input.get()))

    row = cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login successful')
    else:
        messagebox.showinfo('info', 'login failed')
        
    cursor.connection.commit()
    app.close()

window = tk.Tk()
window.title("USER LOGIN")
window.geometry("400x300")
window['background']='#856ff8'
# window.mainloop()

padd = 20
window["padx"] = padd
user_input = tk.StringVar()
password_input = tk.StringVar()


font_letter =  font.Font(weight="bold")
info_label = tk.Label(window, text="Login application")
info_label.grid(row=0, column=0, pady=20)
info_label['background']='#856ff8'
info_label['font'] = font_letter



info_user_label = tk.Label(window, text="Username")
info_user_label.grid(row=1, column=0)
user_input=  tk.Entry(window,textvariable=user_input)
user_input.grid(row=1, column=1)
info_user_label['background']='#856ff8'
info_user_label['font'] = font_letter


info_password_label = tk.Label(window, text="Password")
info_password_label.grid(row=2, column=0, pady=20)
password_input=  tk.Entry(window, textvariable=password_input)
password_input.grid(row=2, column=1)
info_password_label['background']='#856ff8'
info_password_label['font'] = font_letter

login_button = tk.Button(window, text= 'Login', command=login)
login_button.grid(row=3,column=1)


window.mainloop()