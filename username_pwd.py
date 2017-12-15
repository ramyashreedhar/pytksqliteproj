import sqlite3 as lite
import sys
from tkinter import *


def getusername():
    text = TextEntry.get()
    name = str(text)
    pwd = TextEntry2.get()
    passcode = str(pwd)
    con = lite.connect('C:/Users/RamsRalz/Documents/Android/SDK/tools/logindb')
    if con:
        print('db connected')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM loguser")
        rows = cur.fetchall()
        for row in rows:
            if name and passcode in row:
                lbl2.config(text='ACCESS GRANTED!LOGIN SUCCESSFUL SINCE USER IS ALREADY REGISTERED')
                break

            else:
                lbl2.config(text='ACCESS DENIED!PLEASE REGISTER')

    return lbl2

def registeruser():
    text = TextEntry.get()
    name = str(text)
    pwd = TextEntry2.get()
    passcode = str(pwd)
    con = lite.connect('C:/Users/RamsRalz/Documents/Android/SDK/tools/logindb')
    if con:
        print('db connected')
    getusername()
    if lbl2.cget("text")=='ACCESS DENIED!PLEASE REGISTER':
        with con:
            cur = con.cursor()
            cur.execute('''INSERT INTO loguser(username,password) VALUES(?,?)''', (name, passcode))
            con.commit()

            print('Newly Registere User:')
            cur.execute('SELECT * FROM loguser ORDER BY rowid DESC LIMIT 1')
            row=cur.fetchone()
            print(row)
            lbltxt.config(text="USER REGISTERED SUCCESSFULLY! YOU CAN LOGIN")








window = Tk()
window.geometry("300x250")
window.title("username password screen")
window.configure(background='#DEEFF5')
lbl=Label(window,text="enter the username")
lbl.configure(background='#DEEFF5')
lbl.pack()
TextEntry=Entry(window,bd=5)
TextEntry.pack()
lbl3=Label(window,text="enter the password")
lbl3.configure(background='#DEEFF5')
lbl3.pack()
TextEntry2=Entry(window,bd=5)
TextEntry2.pack()
Button1=Button(window,text="Login",padx=20,command=getusername)
Button1.pack()
lbl2=Label(window,text="")
lbl2.configure(background='#DEEFF5')
lbl2.pack()
Button2=Button(window,text='Register',padx=20,command=registeruser)
Button2.pack()
lbltxt=Label(window,text="")
lbltxt.configure(background='#DEEFF5')
lbltxt.pack()
mainloop()