from glob import glob
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector

root = tk.Tk()

root.title("ATM - CRUD")
root.iconphoto(False, tk.PhotoImage(file='CITC.png'))
root.geometry('1920x1080')

bg = PhotoImage(file = "atm_background_login.png")
bg_label = Label(root, image = bg)
bg_label.place(x=0, y=0, relwidth = 1, relheight= 1)

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="dbactivity3"
)

def btn_insert():
    mycursor = mydb.cursor()
    sql = "INSERT INTO tblusers (id, username, password, balance) VALUES (%s, %s, %s, %s)"
    val = (input_id.get(), input_username.get(), input_password.get(), input_balance.get())
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    input_id.delete(0, END)
    input_username.delete(0, END)
    input_password.delete(0, END)
    input_balance.delete(0, END)

    messagebox.showinfo("Insered", "A new data has been created!")

def retrieve_data(id):
    mycursor = mydb.cursor()
    sql = "SELECT id, username, password, balance FROM tblusers WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mycursor.close()
    return result

def btn_select():
    id = input_id.get()
    result = retrieve_data(id)
    if result:
        input_username.delete(0, END)
        input_username.insert(0, result[1])
        input_password.delete(0, END)
        input_password.insert(0, result[2])
        input_balance.delete(0, END)
        input_balance.insert(0, result[3])
        response = messagebox.showinfo("Selected", "Data has been retrieved!")
    else:
        messagebox.showerror("Error", "ID not found")

def btn_update():
    mycursor = mydb.cursor()
    sql = "UPDATE tblusers SET username = %s, password = %s, balance = %s WHERE id = %s"
    val = (input_username.get(), input_password.get(), input_balance.get(), input_id.get())
    mycursor.execute(sql, val)
    mydb.commit()

    input_id.delete(0, END)
    input_username.delete(0, END)
    input_password.delete(0, END)
    input_balance.delete(0, END)

    messagebox.showinfo("Update", "Data has been updated!")

def btn_delete():
    mycursor = mydb.cursor()
    sql = "DELETE FROM tblusers WHERE id = %s"
    val = (input_id.get(), )
    mycursor.execute(sql, val)
    mydb.commit()

    input_id.delete(0, END)
    input_username.delete(0, END)
    input_password.delete(0, END)
    input_balance.delete(0, END)

    messagebox.showinfo("Delete", "Data has been deleted!")

def clear_id(event):
    input_id.delete(0, END)

def clear_username(event):
    input_username.delete(0, END)

def clear_password(event):
    input_password.delete(0, END)

def clear_balance(event):
    input_balance.delete(0, END)

input_id = Entry(root, textvariable='id', font=("Integral CF", 25, 'bold'))
input_id.config(fg='#a6a6a6', bg='white', insertwidth=1, insertofftime=1000, borderwidth=0, highlightthickness=0, justify="center")
input_id.insert(0, "Input your ID")
input_id.bind("<Button-1>", clear_id)
input_id.place(relx=0.5, rely=0.3, anchor="center")

entry_username = PhotoImage(file='placeholder_login.png')
placeholder_username = Label(root, image=entry_username, border=0)
placeholder_username.config(bg="white")
placeholder_username.place(x=0, y=400, relx=0.5, anchor="center")

input_username = Entry(root, textvariable='username', font=("Poppins", 20, 'bold'), width=26, border=0)
input_username.config(fg='#13136b', bg='#e9e9e9', insertwidth=1, insertofftime=1000)
input_username.insert(0, "Username")
input_username.bind("<Button-1>", clear_username)
input_username.place(x=0, y=403, relx=0.5, anchor="center")

entry_password = PhotoImage(file='placeholder_login.png')
placeholder_password = Label(root, image=entry_password, border=0)
placeholder_password.config(bg="white")
placeholder_password.place(x=0, y=500, relx=0.5, anchor="center")

input_password = Entry(root, textvariable='password', font=("Poppins", 20, 'bold'), width=26, border=0)
input_password.config(fg='#13136b', bg='#e9e9e9', insertwidth=1, insertofftime=1000)
input_password.insert(0, "Password")
input_password.bind("<Button-1>", clear_password)
input_password.place(x=0, y=503, relx=0.5, anchor="center")

entry_balance = PhotoImage(file='placeholder_login.png')
placeholder_balance = Label(root, image=entry_balance, border=0)
placeholder_balance.config(bg="white")
placeholder_balance.place(x=0, y=600, relx=0.5, anchor="center")

input_balance = Entry(root, textvariable='balance', font=("Poppins", 20, 'bold'), width=26, border=0)
input_balance.config(fg='#13136b', bg='#e9e9e9', insertwidth=1, insertofftime=1000)
input_balance.insert(0, "Balance")
input_balance.bind("<Button-1>", clear_balance)
input_balance.place(x=0, y=603, relx=0.5, anchor="center")

init_insert = PhotoImage(file='insert.png')
insert = Button(root, image = init_insert, borderwidth = 0, command = btn_insert)
insert.config(bg = "white")
insert.place(x=0, y=710, relx=0.422, anchor="center")

init_select = PhotoImage(file='select.png')
select = Button(root, image = init_select, borderwidth = 0, command = btn_select)
select.config(bg = "white")
select.place(x=0, y=710, relx=0.578, anchor="center")

init_update = PhotoImage(file='update.png')
update = Button(root, image = init_update, borderwidth = 0, command = btn_update)
update.config(bg = "white")
update.place(x=0, y=780, relx=0.422, anchor="center")

init_delete = PhotoImage(file='delete.png')
delete = Button(root, image = init_delete, borderwidth = 0, command = btn_delete)
delete.config(bg = "white")
delete.place(x=0, y=780, relx=0.578, anchor="center")

root.mainloop() 