#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt

sess = None

def register(fname, lname, email, password):
    #print display("home.html").render(username=username)
    enc_password = sha512_crypt.encrypt(password) 

    command = "INSERT INTO Users(fname, lname, email, password) VALUES(%s, %s, %s, %s)"
    try:
        cur = con.cursor()
        cur.execute(command, (fname, lname, email, enc_password))      
        con.commit()

    except mdb.Error, e:
        if con:
            con.rollback()

    print "Location: home.py?name=" + fname + "\r\n"

def main():
    form = cgi.FieldStorage()

    password = form.getvalue('password')
    fname = form.getvalue('fname')
    lname = form.getvalue('lname')
    email = form.getvalue('email')
    email_exists = False
    #username_exists = False
    
    #From registration, verifies that email and username are unique#if username_exists:
    #    print display("reg.html").render()
    #    print "<script type='text/javascript'> \
    #            alert('Username is taken. Please choose another.');\
    #            </script>"
    try:
        cur = con.cursor()

        # Checks if email is unique
        command = "SELECT email FROM Users"
        cur.execute(command)
        for i in range(cur.rowcount):
            row = cur.fetchone()
            if(email == row[0]):
                email_exists = True

        #Checks if username is unique
        #command = "SELECT username FROM Users"
        #cur.execute(command)
        #for i in range(cur.rowcount):
        #    row = cur.fetchone()
        #    if(username == row[0]):
        #        username_exists = True
        
    except mdb.Error, e:
        if con:
            con.rollback()

    #if username_exists:
    #    print display("reg.html").render()
    #    print "<script type='text/javascript'> \
    #            alert('Username is taken. Please choose another.');\
    #            </script>"
    if email_exists:
        print "Location: index.py?redirect=0\r\n"
    else:
        register(fname, lname, email, password)
	

if __name__ == '__main__':
    main()
