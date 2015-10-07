#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json

def cookieValidationFailed():
	print display("login.html").render()
	print "<script type='text/javascript'> \
	          alert('Session Expired. Please log in.');\
	          </script>" 

def invaidPageError():
	print display("login.html").render()
	print "<script type='text/javascript'> \
	          alert('Error occurred. Please try again.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	
	fname = form.getvalue('fname')
	lname = form.getvalue('lname')
	genre = form.getvalue('genre')
	sess = session.Session(expires=365*24*60*60, cookie_path='/')

	if(lname and fname):

		if(genre != None):
			command = "SELECT * from Books NATURAL JOIN Genres WHERE Genre='" + genre + "'"
		else:
			command = "SELECT * from Books"
		
		try:
			cur = con.cursor()
			cur.execute(command)
			con.commit()
			rows = cur.fetchall()

			titles = []
			for row in rows:
				titles.append(row)
			print display("home.html").render(fname=fname,lname=lname,titles=titles,genre=genre)
			
		except mdb.Error, e:
			if con:
				con.rollback()
	else:
		invaidPageError()

if __name__ == '__main__':
	main()