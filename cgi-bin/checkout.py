#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json

def main():
	form = cgi.FieldStorage()
	
	email = form.getvalue('email') #email of current user

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() 

		print display("checkout.html").render(user=user_)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()