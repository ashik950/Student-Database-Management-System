from tkinter import *
import sys
from tkinter import ttk, messagebox
import MySQLdb

db=MySQLdb.connect("localhost","root","","db_mgmt")
conn=db.cursor()  

def verifier():
    a=b=c=d=e=f=g=0
    if not staff_name.get():
        t1.insert(END,"<>Staff name is required<>\n")
        a=1
    if not sid.get():
        t1.insert(END,"<>Staff id is required<>\n")
        b=1
    if not desig.get():
        t1.insert(END,"<>Designation is required<>\n")
        c=1
    if not quali1.get():
        t1.insert(END,"<>Qualification is required<>\n")
        d=1
    if not exp.get():
        t1.insert(END,"<>Experience is required<>\n")
        e=1    
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        f=1
    
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        g=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1:
        return 1
    else:
        return 0


def add_staff():
            ret=verifier()
            if ret==0:
              
                sin=ls.curselection() 
                did=int(ls.get(sin[0]))               
                conn.execute("insert into staff values('%s','%d','%d','%s','%s','%s','%s','%s')"%(staff_name.get(),int(sid.get()),int(did),desig.get(),quali1.get(),exp.get(),phone.get(),address.get()))
                db.commit()
                
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_staff():
   
    conn.execute("select * from staff")
    data=conn.fetchall()    
    for i in data:
        t1.insert(END,str(i)+"\n")

def view_staff1():
    
    conn.execute("select * from STAFF where STAFFID=%d"%(int(sid.get())))
    #data=cur.fetchall()
    ls.delete(0,END)
    row=conn.fetchone();
    if (row is not None):
        e1.insert(0,row[0])
        #e2.insert(0,row[1])
        a=row[2]
        ls.insert(0,a)
        
        e3.insert(0,row[3])
        e4.insert(0,row[4])
        e5.insert(0,row[5])
        e6.insert(0,row[6])
        e7.insert(0,row[7])
    else:
        messagebox.showinfo("Error: ","Staff ID Not Found")
        
def delete_staff():
    ret=verifier()
    if ret==0:
        
        conn.execute("DELETE FROM STAFF WHERE staffid=%d"%(int(sid.get())))
        db.commit()        
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_staff():
    ret=verifier()
    if ret==0:        
        sin=ls.curselection() 
        did=int(ls.get(sin[0]))
        conn.execute("UPDATE STAFF SET NAME='%s',DID=%d,DESIG='%s',QUALI='%s',EXP='%s',PHONE_NO='%s',ADDR='%s' where STAFFID=%d"%(staff_name.get(),int(did),desig.get(),quali1.get(),exp.get(),phone.get(),address.get(),int(sid.get())))
        db.commit()        
        t1.insert(END,"UPDATED SUCCESSFULLY\n")

def clear():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
    e3.delete(0,len(e3.get()))
    e4.delete(0,len(e4.get()))
    e5.delete(0,len(e5.get()))
    e6.delete(0,len(e6.get()))
    e7.delete(0,len(e7.get()))
    t1.delete(1.0,END)
    ls.delete(0,END)
    conn.execute("select did from dept")
    row=conn.fetchall()
    i=0
    for row1 in row:
        ls.insert(i,row1[0])
        i+=1
        
def close():
    root.destroy()


if __name__=="__main__":
    root=Tk()
    root.title("Database Management System-Staff Details")
     
    staff_name=StringVar()
    sid=StringVar()
    desig=StringVar()
    quali1=StringVar()
    exp=StringVar()
    phone=StringVar()
    address=StringVar()
    
    label1=Label(root,text="Staff Name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Staff Id:")
    label2.place(x=0,y=30)

    label3=Label(root,text="Department Id:")
    label3.place(x=0,y=60)    
    
    label4=Label(root,text="Designation:")
    label4.place(x=0,y=130)

    label5=Label(root,text="Qualification:")
    label5.place(x=0,y=160)

    label6=Label(root,text="Experience:")
    label6.place(x=0,y=200)
    
    label7=Label(root,text="Phone Number:")
    label7.place(x=0,y=230)

    label8=Label(root,text="Address:")
    label8.place(x=0,y=260)

    e1=Entry(root,textvariable=staff_name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=sid)
    e2.place(x=100,y=30)

    ls=Listbox(root,height=3,selectmode="single")
    ls.place(x=100,y=60)

    conn.execute("select did from dept")
    row=conn.fetchall()
    i=0
    for row1 in row:
        ls.insert(i,row1[0])
        i+=1
        
    e3=Entry(root,textvariable=desig)
    e3.place(x=100,y=130)
    
    e4=Entry(root,textvariable=quali1)
    e4.place(x=100,y=200)

    e5=Entry(root,textvariable=exp)
    e5.place(x=100,y=160)
    
    e6=Entry(root,textvariable=phone)
    e6.place(x=100,y=240)
        
    e7=Entry(root,textvariable=address)
    e7.place(x=100,y=280)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)  


    b1=Button(root,text="ADD STAFF",command=add_staff,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STAFFS",command=view_staff,width=40)
    b2.grid(row=12,column=0)
    
    b6=Button(root,text="VIEW STAFFS",command=view_staff1,width=40)
    b6.grid(row=13,column=0)
    
    b3=Button(root,text="DELETE STAFF",command=delete_staff,width=40)
    b3.grid(row=14,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_staff,width=40)
    b4.grid(row=15,column=0)

    b5=Button(root,text="CLEAR",command=clear,width=40)
    b5.grid(row=16,column=0)
    
    b6=Button(root,text="CLOSE",command=close,width=40)
    b6.grid(row=17,column=0)


    root.mainloop()
