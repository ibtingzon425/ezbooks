#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json
import utilities

def main():
	form = cgi.FieldStorage()
	
	email = form.getvalue('email') #email of current user

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() 
		
		sidebar = utilities.getSideBar(email, user_[9], cur)
		print display("checkout.html").render(sidebar=sidebar,user=user_)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
