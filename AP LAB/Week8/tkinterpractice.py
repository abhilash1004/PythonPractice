from tkinter import *
import sqlite3
window = Tk()
window.geometry("700x500")
def db():
    con=sqlite3.connect('details3.db')
    con.execute('''CREATE TABLE IF NOT EXISTS DETAILS(name varchar(10),age varchar(4))''')
    #print(name,date)
    con.execute('insert into details (name,age) values (?,?)',(name.get(),date.get()))
    cur=con.execute('''SELECT * FROM DETAILS''')
    con.commit()
    for i in cur:
        print(i)

def f():
    p=open("test.txt","a+")
    p.write("\nName:"+str(name.get()))
    p.close()
def fun():
    Label(text="Your age:"+str(date.get())).grid(row=10,column=10)
    f=open("test.txt","a+")
    f.write(str(date.get()))
    f.close()

nameLable = Label(text="Name:").grid(row=0,column=0,padx=10,pady=10)
phoneLable = Label(text="Phone:").grid(row=1,column=0,padx=10,pady=10)
dateLable = Label(text="Bday:").grid(row=2,column=0,padx=10,pady=10)
name = StringVar()
phone = StringVar()
date = StringVar()
nameEntry = Entry(window, textvariable=name).grid(row=0,column=1,padx=10,pady=10)
phoneEntry = Entry(window, textvariable=phone).grid(row=1,column=1,padx=10,pady=10)
dateEntry = Entry(window, textvariable=date).grid(row=2,column=1,padx=10,pady=10)
b = Button(text="age calculator",command=fun).grid(row=5,column=6)
b1=Button(text="write",command=f).grid(row=6,column=6)
b2=Button(text="write to db",command=db).grid(row=7,column=6)
# con = sqlite3.connect('details.db')
# cur =con.execute('select * from details')
# for i in cur:
#     print(i)
# print('Hello')
window.mainloop()