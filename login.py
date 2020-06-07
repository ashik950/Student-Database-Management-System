import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

root = tk.Tk()
root.title("Management")


appLabel = tk.Label(root, text="Database Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class login:
    UserName = ""
    Password = "" 

    def __init__(self, UserName, Password):
        self.UserName  = studentName
        self.Password = collegeName
     

nameLabel = tk.Label(root, text="Enter your  username", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
pwdLabel = tk.Label(root, text="Enter your password", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))


nameEntry = tk.Entry(root, width = 30)
pwdEntry = tk.Entry(root, width = 30,show='*')


nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
pwdEntry.grid(row=2, column=1, padx=(0,10), pady = 20)


def takeNameInput():
    global nameEntry, pwdEntry

    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    pwd = pwdEntry.get()
    pwdEntry.delete(0, tk.END)   

    if(username=="admin" and pwd=="admin"):
       os.system('python master.py')
             
    else:
         messagebox.showinfo("Error: ", "Invalid Username/Password")


def destroyRootWindow():
    root.destroy()

button = tk.Button(root, text="Login", width=45,command=lambda :takeNameInput())
button.grid(pady=25, row=3, columnspan=2)

##button.grid(row=5, column=0)
##
##displayButton = tk.Button(root, text="Logout", command=lambda :destroyRootWindow())
##displayButton.grid(row=5, column=1)

root.mainloop()
