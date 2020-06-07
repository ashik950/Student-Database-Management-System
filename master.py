from tkinter import *
import os

if __name__=="__main__":
    root=Tk()
    root.wm_minsize(1000,500)
    root.title("Database Management System")
     
def show1():
    os.system('python dept.py')
def show2():
     os.system('python staff.py')
def show3():
     os.system('python student.py')

menubar=Menu(root)

arithmenu=Menu(menubar,tearoff=0)
arithmenu.add_command(label="Department", command=show1)
arithmenu.add_command(label="Staff", command=show2)
arithmenu.add_command(label="Student",command=show3)
menubar.add_cascade(label="Options" ,menu=arithmenu)
root.config(menu=menubar)
root.mainloop()



