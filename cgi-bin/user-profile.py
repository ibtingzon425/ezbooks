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
	
	userprof = form.getvalue('user') #email of userprofile
	email = form.getvalue('email') #email of current user

	#TODO: If current user != email 

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() #

		command = "SELECT * FROM Users WHERE Email = '" + userprof + "'";
		cur.execute(command)
		userprof = cur.fetchone() #

		command = "SELECT * from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		command = "SELECT * from ComicBooks NATURAL JOIN UserOwned WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		own = []
		for row in rows:
			own.append(row)

		print display("user-profile.html").render(user=user,userprof=userprof,titles=titles,own=own)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()