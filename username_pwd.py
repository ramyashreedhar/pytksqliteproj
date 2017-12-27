'''

This is a simple login application using Python and Tkinter GUI.

'''
import re
import sqlite3 as lite
import sys
from tkinter import *
'''----------------------------------------------------------------------------------------------------------------------'''
'''Configurable  db path'''

LOGINDB = 'C:/Users/RamsRalz/Documents/Android/SDK/tools/logindb'

'''-------------------------------------------------------------------------------------------------------------------------------'''
'''
  Functions Start here
'''
'''-------------------------------------------------------------------------------------------------------------------------------'''
'''Name:validateusername(str username)
   Desc:Accepts the username entered and validates the same
   arguments:username entry string
   return type:boolean
   returns False if pattern does not match

'''
'''--------------------------------------------------------------------------------------------------------------'''
def validateusername(username):
    pattern="^[a-zA-Z0-9]{6,15}$"
    '''
    pattern description:
    ^        # Start of the line
  [a-zA-z0-9] # Match characters and symbols in the list, a-z,A-Z, 0-9
   {6,15}    # Length at least 6 characters and maximum length of 15
    $        # End of the line
    '''
    #username='Padma1'
    result = re.match(pattern, username)

    if not(result):
        print('Invalid username. Please check')
        return False
    else:
        return True

'''-------------------------------------------------------------------------------------------------------------------------------'''
'''Name:validateusername(str username)
   Desc:Accepts the username entered and validates the same
   arguments:username entry string
   return type:boolean
   returns False if pattern does not match

'''
'''--------------------------------------------------------------------------------------------------------------'''
def validatepwd(password):
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    '''
    pattern description
     ^               # Start of the line
     .*(?=.{8,})     # minimum length of 8
     (?=.*\d)        # numbers 0-9
     (?=.*[a-z])     # lowercase alphabets
     (?=.*[A-Z])     # uppercase alphabets
     (?=.*[@#$%^&+=] # special characters
     $               # End of the line
     
    '''
    #password='Pass1w$0'
    result = re.match(pattern, password)
    if not(result):
        print(" Invalid password ")
        return False
    else:
        return True
'''----------------------------------------------------------------------------------------------------------'''
'''Name:getusername()
   Desc:Checks if the entered username and password is already registered  in db or not
   Checks if the username and passwords match or not
   return type:none
   Returns success message on success or error message otherwise
   
'''
'''----------------------------------------------------------------------------------------------------------'''
def getusername():
    global LOGINDB
    name= TextEntry.get()

    pwd = TextEntry2.get()


    try:
        con = lite.connect(LOGINDB)
        if con:
            print('db connected')
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM loguser")
            rows = cur.fetchall()
            print(type(rows))
            for row in rows:
                if (name in row and pwd not in row)or (name not in row and pwd in row):
                    lbl2.config(text='UserName and Password don\'t match')
                    break


                elif name in row and pwd in row:
                    lbl2.config(text='ACCESS GRANTED!LOGIN SUCCESSFUL SINCE USER IS ALREADY REGISTERED')
                    break

                else:
                    lbl2.config(text='ACCESS DENIED!PLEASE REGISTER')


    except lite.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)
    except:
        print("Unknown exception occured in db ")
        sys.exit(1)
'''----------------------------------------------------------------------------------------------------------'''
'''
Name   :registeruser
Desc   : checks if users are already registered and if not  registers the user by inserting the user in the db

Arguments :  none
Return type: none 
Displays: 'Newly Registered User:(
                                                          
'''
'''----------------------------------------------------------------------------------------------------------'''
def registeruser( ):
    name = TextEntry.get()
    valname=validateusername(name)
    pwd = TextEntry2.get()
    valpwd=validatepwd(pwd)

    try:
        con = lite.connect(LOGINDB)


        if con:
            print('db connected')
        getusername()
        if lbl2.cget("text")=='ACCESS DENIED!PLEASE REGISTER':
            if not(valname and valpwd):
                lblval.config(text="Invalid username/password!")
                sys.exit(1)
            else:
                with con:
                    cur = con.cursor()
                    cur.execute('''INSERT INTO loguser(username,password) VALUES(?,?)''', (name, pwd))
                    con.commit()

                    print('Newly Registered User:')
                    cur.execute('SELECT * FROM loguser ORDER BY rowid DESC LIMIT 1')
                    row=cur.fetchone()
                    print(row)

                    lbltxt.config(text="USER REGISTERED SUCCESSFULLY! YOU CAN LOGIN!")
                    lblreguser.config(text="New Registered User: ('%s','%s')" % (name,pwd))

    except lite.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)
    except:
        print("Unknown exception occured in registeruser ")
        sys.exit(1)



'''--------------------------------------------------------------------------------------------------------------------------'''

'''The Main Program runs here'''
'''-----------------------------------------------------------------------------------------------------------------------------------'''

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
lblval=Label(window,text="")
lblval.configure(background='#DEEFF5')
lblval.pack()
lblreguser=Label(window,text="")
lblreguser.configure(background='#DEEFF5')
lblreguser.pack()
mainloop()

'''----------------------------------------------------------------------------------------------------------------------'''

'''-------------------------------END OF FILE-------------------------------------------------------------------------------------------------------------------'''