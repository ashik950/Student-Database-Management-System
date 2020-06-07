from tkinter import *
import sys
from tkinter import ttk, messagebox
import MySQLdb

db=MySQLdb.connect("localhost","root","","db_mgmt")
conn=db.cursor()
  


def verifier():
    a=b=0
    if not did.get():
        t1.insert(END,"<>department id is required<>\n")
        a=1
    if not dname.get():
        t1.insert(END,"<>department name is required<>\n")
        b=1   
   
    if a==1 or b==1 :
        return 1
    else:
        return 0



def add_dept():
            ret=verifier()
            if ret==0:      
               
                conn.execute("insert into dept values('%d','%s')"%(int(did.get()),dname.get()))
                db.commit()
                
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_dept():
    
    #cur=conn.cursor()
    conn.execute("select * from DEPT")
    data=conn.fetchall()
   
    for i in data:
        t1.insert(END,str(i)+"\n")

def view_dept1():
    
    #cur=conn.cursor()
    conn.execute("select * from dept where did=%d"%(int(did.get())))
    #data=cur.fetchall()
    
    row=conn.fetchone();
    if (row is not None):
        #e1.insert(0,row[0])
        e2.insert(0,row[1])
        
    else:
        messagebox.showinfo("Error: ","Student ID Not Found")
        
def delete_dept():
    ret=verifier()
    if ret==0:
       
        #cur=conn.cursor()
        conn.execute("DELETE FROM DEPT WHERE DID=%d"%(int(did.get())))
        db.commit()
       
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_dept():
    ret=verifier()
    if ret==0:
       
        #cur=conn.cursor()
        conn.execute("UPDATE DEPT SET DNAME='%s' where DID=%d"%(dname.get(),int(did.get())))
        db.commit()
       
        t1.insert(END,"UPDATED SUCCESSFULLY\n")

def clear():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
    t1.delete(1.0,END)
    
def close():
    root.destroy()


if __name__=="__main__":
    root=Tk()
    root.wm_minsize(1000,500)
    root.title("Database Management System-Department Details")
     
    did=StringVar()
    dname=StringVar()   
    
    
    label1=Label(root,text="Department Id:")
    label1.place(x=0,y=20)

    label2=Label(root,text="Department Name:")
    label2.place(x=0,y=60)

    e1=Entry(root,textvariable=did)
    e1.place(x=100,y=20)

   
    #cur=conn.cursor()

    #cur.execute("CREATE TABLE IF NOT EXISTS DEPT(DID INT,DNAME TEXT)")

    conn.execute("select count(DID) from DEPT")
    row=conn.fetchall()
    
    for row1 in row:
        e1.insert(0,(int(str(row1[0]))+1))
    
    
    e2=Entry(root,textvariable=dname)
    e2.place(x=100,y=60)

    b1=Button(root,text="ADD DEPARTMENT",command=add_dept,width=40)
    #b1.grid(row=11,column=0)
    b1.place(x=0,y=100)

    b2=Button(root,text="VIEW ALL DEPARTMENT",command=view_dept,width=40)
    b2.place(x=0,y=150)
    
    b6=Button(root,text="VIEW DEPARTMENTS",command=view_dept1,width=40)
    b6.place(x=0,y=200)
    
    b3=Button(root,text="DELETE DEPARTMENT",command=delete_dept,width=40)
    b3.place(x=0,y=250)

    b4=Button(root,text="UPDATE INFO",command=update_dept,width=40)
    b4.place(x=0,y=300)

    b5=Button(root,text="CLEAR",command=clear,width=40)
    b5.place(x=0,y=350)
    
    b6=Button(root,text="CLOSE",command=close,width=40)
    b6.place(x=0,y=400)

    t1=Text(root,width=80,height=20)
    t1.place(x=300,y=40)
    
    root.mainloop()
