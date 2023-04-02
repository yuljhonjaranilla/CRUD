from glob import glob
from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("ATM - Home")
root.iconphoto(False, tk.PhotoImage(file='CITC.png'))
root.geometry('1920x1080')

bg = PhotoImage(file = "atm_background_login.png")
bg_label = Label(root, image = bg)
bg_label.place(x=0, y=0, relwidth = 1, relheight= 1)

def on_entry_click_username(event):
    if input_username.get() == 'Username':
        input_username.delete(0, "end")
        input_username.config(fg='#13136b')

def on_entry_click_password(event):
    if input_password.get() == 'Password':
        input_password.delete(0, "end")
        input_password.config(fg='#13136b')

def btn_login():
    pass

def btn_register():
    pass


submit = Label(root, text = "LOGIN YOUR ACCOUNT", font = ("Integral CF", 25, 'bold'))
submit.config(fg = '#13136b', bg = 'white')
submit.place(x=735, y=300)

entry_username = PhotoImage(file='placeholder_login.png')
placeholder_username = Label(root, image=entry_username, border=0)
placeholder_username.config(bg="white")
placeholder_username.place(x=650, y=380)

input_username = Entry(root, textvariable='username', font=("Poppins", 20, 'bold'), width=26, border=0)
input_username.config(fg='#a6a6a6', bg='#e9e9e9', insertwidth=1, insertofftime=1000)
input_username.insert(0, "Username")
input_username.bind('<FocusIn>', on_entry_click_username)
input_username.place(x=700, y=397)

entry_password = PhotoImage(file='placeholder_login.png')
placeholder_password = Label(root, image=entry_password, border=0)
placeholder_password.config(bg="white")
placeholder_password.place(x=650, y=490)

input_password = Entry(root, textvariable='password', font=("Poppins", 20, 'bold'), width=26, border=0)
input_password.config(fg='#a6a6a6', bg='#e9e9e9', insertwidth=1, insertofftime=1000)
input_password.insert(0, "Password")
input_password.bind('<FocusIn>', on_entry_click_password)
input_password.place(x=700, y=507)

init_login = PhotoImage(file='login.png')
login = Button(root, image = init_login, borderwidth = 0, command = btn_login)
login.config(bg = "white")
login.place(x = 650, y = 630)

init_register = PhotoImage(file='register.png')
register = Button(root, image = init_register, borderwidth = 0, command = btn_register)
register.config(bg = "white")
register.place(x = 650, y = 730)


root.mainloop() 