#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json

def invaidPageError():
	print "<script type='text/javascript'> \
	          alert('Error occurred. Please try again.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	
	email = form.getvalue('email')
	genre = form.getvalue('genre')
	sess = session.Session(expires=365*24*60*60, cookie_path='/')

	try:
		cur = con.cursor()

		command = "SELECT FirstName, LastName FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		row = cur.fetchone()
		fname = row[0]
		lname = row[1]

		if(genre != None):
			command = "SELECT * from Books NATURAL JOIN Genres WHERE Genre='" + genre + "'"
		else:
			command = "SELECT * from Books"
			
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)
			
		print display("home.html").render(email=email,fname=fname,lname=lname,titles=titles,genre=genre)

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    print "Location: login.py?error=1"

if __name__ == '__main__':
	main()