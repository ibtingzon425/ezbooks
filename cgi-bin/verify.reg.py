#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json
import utilities

sess = None

def register(fname, lname, email, password):
    enc_password = sha512_crypt.encrypt(password) 

    command = "INSERT INTO Users(FirstName, LastName, Email, Password, DateJoined) VALUES(%s, %s, %s, %s, NOW())"
    try:
        cur = con.cursor()
        cur.execute(command, (fname, lname, email, enc_password))      
        con.commit()

    except mdb.Error, e:
        if con:
            con.rollback()

    sess = session.Session(expires=365*24*60*60, cookie_path='/')
    sess.data['lastvisit'] = repr(time.time())
    sess.data['user'] = email

    print "Location: home.py\r\n"

def main():
    form = cgi.FieldStorage()

    password = form.getvalue('password')
    cpass = form.getvalue('confpwd')
    fname = form.getvalue('fname')
    lname = form.getvalue('lname')
    email = form.getvalue('email')
    email_exists = False
    
    #From registration, verifies that password and cpass are the same
    if(password != cpass):
        print "Location: index.py?redirect=1\r\n"
    else:
        try:
            cur = con.cursor()
            # From registration, verifies if email is unique
            command = "SELECT email FROM Users"
            cur.execute(command)
            for i in range(cur.rowcount):
                row = cur.fetchone()
                if(email == row[0]):
                    email_exists = True

        except mdb.Error, e:
            if con:
                con.rollback()
        if email_exists:
            print "Location: index.py?redirect=0\r\n"
        else:
            register(fname, lname, email, password)
	

if __name__ == '__main__':
    main()
