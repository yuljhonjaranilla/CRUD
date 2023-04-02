from glob import glob
from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("ATM - Home")
root.iconphoto(False, tk.PhotoImage(file='CITC.png'))
root.geometry('1920x1080')

bg = PhotoImage(file = "atm_background.png")
bg_label = Label(root, image = bg)
bg_label.place(x=0, y=0, relwidth = 1, relheight= 1)

def btn_initial():
    global total_cash

    cash = int(input.get()) 
    total_cash = total_cash + cash 
    initial_balance['state'] = DISABLED

    input.delete(0, END)

def btn_remaining():
    global total_cash
    inputbalance.destroy()

    balance = Label(root, text = str(total_cash), font = ("Integral CF", 28))
    balance.config(fg = '#13136b', bg = 'white')
    balance.place(x = 70, y = 450)

    input.delete(0, END)

def btn_deposit():
    global total_cash

    cash = int(input.get())

    total_cash = total_cash + cash
    input_balance = Label(root, text = str(cash), font = ("Integral CF", 28))
    input_balance.config(fg = '#13136b', bg = 'white')
    input_balance.place(x = 70, y = 600)

    deposit = Label(root, text = "Your Deposit:", font = ("Poppins", 20, 'bold'))
    deposit.config(fg = '#fbb414', bg = 'white')
    deposit.place(x = 70, y = 560)

    input.delete(0, END)


def btn_withdraw():
    global total_cash

    cash = int(input.get())

    total_cash = total_cash - cash
    input_balance = Label(root, text = str(total_cash), font = ("Integral CF", 30))
    input_balance.config(fg = '#ff0000', bg = 'white')
    input_balance.place(x = 70, y = 800)

    withdraw = Label(root, text = "Total Balance:", font = ("Poppins", 20, 'bold'))
    withdraw.config(fg = '#13136b', bg = 'white')
    withdraw.place(x = 70, y = 760)

    input.config(fg ='#2a9202', bg = '#e9e9e9', font = ("Integral CF", 28))
    input.place(x = 990, y = 785)

    quickcash = Button(root, text = "Quick Cash  >", borderwidth = 0, font = ("Integral CF", 28))
    quickcash.config(bg = '#e9e9e9', fg = '#2a9202')
    quickcash.place(x = 1500, y = 772)

def btn_name():
    global name
    name.destroy()
    myname = str(input.get())
    input_name = Label(root, text = str(myname), font = ("Integral CF", 28))
    input_name.config(fg = '#13136b', bg = 'white')
    input_name.place(x = 70, y = 290)
    name = input_name
    input.delete(0, END)

def btn_exit():
    quit()

total_cash = 500 

submit = Label(root, text = "Submitted by: Yul Jhon O. Jaranilla", font = ("Poppins", 18, 'bold'))
submit.config(fg = '#fbb414', bg = 'white')
submit.place(x = 1400, y = 40)

welcome = Label(root, text = "Welcome,", font = ("Poppins", 20, 'bold'))
welcome.config(fg = '#fbb414', bg = 'white')
welcome.place(x = 70, y = 250)

name = Label(root, text = "[YOUR NAME]", font = ("Integral CF", 28))
name.config(fg = '#13136b', bg = 'white')
name.place(x = 70, y = 290)

balance = Label(root, text = "Current Balance:", font = ("Poppins", 20, 'bold'))
balance.config(fg = '#fbb414', bg = 'white')
balance.place(x = 70, y = 410)

inputbalance = Label(root, text = "0.00", font = ("Integral CF", 28))
inputbalance.config(fg = '#13136b', bg = 'white')
inputbalance.place(x = 70, y = 450)

init_balance = PhotoImage(file='balance_init.png')
initial_balance = Button(root, image = init_balance, borderwidth = 0, command = btn_initial)
initial_balance.config(bg = "white")
initial_balance.place(x = 935, y = 250)

init_deposit = PhotoImage(file='deposit.png')
deposit = Button(root, image = init_deposit, borderwidth = 0, command = btn_deposit)
deposit.config(bg = "white")
deposit.place(x = 1400, y = 250)

rem_balance = PhotoImage(file='balance_rem.png')
remaining_balance = Button(root, image = rem_balance, borderwidth = 0, command = btn_remaining)
remaining_balance.config(bg = "white")
remaining_balance.place(x = 935, y = 400)

cash_withdraw = PhotoImage(file='withdraw.png')
withdraw = Button(root, image = cash_withdraw, borderwidth = 0, command = btn_withdraw)
withdraw.config(bg = "white")
withdraw.place(x = 1400, y = 400)

set_name = PhotoImage(file='name.png')
setname = Button(root, image = set_name, borderwidth = 0, command = btn_name)
setname.config(bg = "white")
setname.place(x = 935, y = 550)

x_exit = PhotoImage(file='exit.png')
exit = Button(root, image = x_exit, borderwidth = 0, command = exit)
exit.config(bg = "white")
exit.place(x = 1400, y = 550)

entry_placeholder = PhotoImage(file='placeholder.png')
placeholder = Label(root, image = entry_placeholder, border = 0)
placeholder.config(bg = "white")
placeholder.place(x = 935, y = 750)

input = Entry(root, textvariable = 'number', font = ("Poppins", 30, 'bold'), width = 18, border = 0)
input.config(fg ='#13136b', bg = '#e9e9e9')
input.place(x = 990, y = 775)

root.mainloop() 