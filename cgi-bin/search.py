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
	search = form.getvalue('search')
	genre = form.getvalue('genre')
	sess = session.Session(expires=365*24*60*60, cookie_path='/')

	#TODO: For fname, lname == None redirect to login page
	#TODO: Implement sessions using Cookies

	try:
		cur = con.cursor()

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone()

		titles = []
		
		if(search != None):
			put = "ISBN, Title, Price, Publisher, Description, Image"
			command = "SELECT " + put + " from Books NATURAL JOIN BookAuthor NATURAL JOIN Authors WHERE AuthorName LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				titles.append(row)

			command = "SELECT " + put + " from Books WHERE ISBN LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				titles.append(row)

			command = "SELECT " + put + " from Books WHERE Title LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				titles.append(row)
		else:
			search = " "
			
		print display("home.html").render(user=user,titles=titles,genre=genre,search=search)

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    print "Location: login.py?error=1"

if __name__ == '__main__':
	main()