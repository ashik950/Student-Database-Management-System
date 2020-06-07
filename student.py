from tkinter import *
import sys
from tkinter import ttk, messagebox
import MySQLdb

db=MySQLdb.connect("localhost","root","","db_mgmt")
conn=db.cursor()  

def verifier():
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"<>Student name is required<>\n")
        a=1
    if not roll_no.get():
        t1.insert(END,"<>Roll no is required<>\n")
        b=1
    if not branch.get():
        t1.insert(END,"<>Batch is required<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not father.get():
        t1.insert(END,"<>Father name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
              
                sin=ls.curselection() 
                did=int(ls.get(sin[0]))
                #conn.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,FATHER TEXT,ADDRESS TEXT)")
                conn.execute("insert into STUDENTS values('%s','%d','%d','%s','%s','%s','%s')"%(student_name.get(),int(roll_no.get()),int(did),branch.get(),phone.get(),father.get(),address.get()))
                db.commit()
                
                t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_student():
   
    conn.execute("select * from STUDENTS")
    data=conn.fetchall()    
    for i in data:
        t1.insert(END,str(i)+"\n")

def view_student1():
    
    conn.execute("select * from STUDENTS where ROLL_NO=%d"%(int(roll_no.get())))
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
    else:
        messagebox.showinfo("Error: ","Student ID Not Found")
        
def delete_student():
    ret=verifier()
    if ret==0:
        
        conn.execute("DELETE FROM STUDENTS WHERE ROLL_NO=%d"%(int(roll_no.get())))
        db.commit()        
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

def update_student():
    ret=verifier()
    if ret==0:        
         
        did=int(ls.get(0))
        conn.execute("UPDATE STUDENTS SET NAME='%s',DID=%d,BRANCH='%s',PHONE_NO='%s',FATHER='%s',ADDRESS='%s' where ROLL_NO=%d"%(student_name.get(),int(did),branch.get(),phone.get(),father.get(),address.get(),int(roll_no.get())))
        db.commit()        
        t1.insert(END,"UPDATED SUCCESSFULLY\n")

def clear():
    e1.delete(0,len(e1.get()))
    e2.delete(0,len(e2.get()))
    e3.delete(0,len(e3.get()))
    e4.delete(0,len(e4.get()))
    e5.delete(0,len(e5.get()))
    e6.delete(0,len(e6.get()))    
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
    root.title("Database Management System-Student Details")
     
    student_name=StringVar()
    roll_no=StringVar()
    branch=StringVar()
    phone=StringVar()
    father=StringVar()
    address=StringVar()
    
    label1=Label(root,text="Student name:")
    label1.place(x=0,y=0)

    label2=Label(root,text="Roll no:")
    label2.place(x=0,y=30)

    label7=Label(root,text="Department Id:")
    label7.place(x=0,y=60)    
    
    label3=Label(root,text="Batch:")
    label3.place(x=0,y=130)

    label4=Label(root,text="Phone Number:")
    label4.place(x=0,y=160)

    label5=Label(root,text="Father Name:")
    label5.place(x=0,y=200)

    label6=Label(root,text="Address:")
    label6.place(x=0,y=230)

    e1=Entry(root,textvariable=student_name)
    e1.place(x=100,y=0)

    e2=Entry(root,textvariable=roll_no)
    e2.place(x=100,y=30)

    ls=Listbox(root,height=3,selectmode="single")
    ls.place(x=100,y=60)

    conn.execute("select did from dept")
    row=conn.fetchall()
    i=0
    for row1 in row:
        ls.insert(i,row1[0])
        i+=1
        
    e3=Entry(root,textvariable=branch)
    e3.place(x=100,y=130)

    e4=Entry(root,textvariable=phone)
    e4.place(x=100,y=160)
    
    e5=Entry(root,textvariable=father)
    e5.place(x=100,y=200)

    e6=Entry(root,textvariable=address)
    e6.place(x=100,y=240)
    
    t1=Text(root,width=80,height=20)
    t1.grid(row=10,column=1)  


    b1=Button(root,text="ADD STUDENT",command=add_student,width=40)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40)
    b2.grid(row=12,column=0)
    
    b6=Button(root,text="VIEW STUDENTS",command=view_student1,width=40)
    b6.grid(row=13,column=0)
    
    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40)
    b3.grid(row=14,column=0)

    b4=Button(root,text="UPDATE INFO",command=update_student,width=40)
    b4.grid(row=15,column=0)

    b5=Button(root,text="CLEAR",command=clear,width=40)
    b5.grid(row=16,column=0)
    
    b6=Button(root,text="CLOSE",command=close,width=40)
    b6.grid(row=17,column=0)


    root.mainloop()
