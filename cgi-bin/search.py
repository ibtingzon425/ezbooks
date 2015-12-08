#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json
import utilities

def invaidPageError():
	print "<script type='text/javascript'> \
	          alert('Error occurred. Please try again.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	
	#email = form.getvalue('email')
	search = form.getvalue('search')
	genre = form.getvalue('genre')

	try:
		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie
		
		if email is None:
			print "Location: login.py?redirect=1\r\n"

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone()

		titles = []
		
		if(search != None):
			put = "ISBN, Title, Price, Publisher, Description, Image"
			command = "SELECT " + put + " from ComicBooks NATURAL JOIN BookWriter NATURAL JOIN Writers WHERE WriterName LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				if row not in titles:
					titles.append(row)

			command = "SELECT " + put + " from ComicBooks WHERE ISBN LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				if row not in titles:
					titles.append(row)

			command = "SELECT " + put + " from ComicBooks WHERE Title LIKE '%" + search + "%'"
			cur.execute(command)
			rows = cur.fetchall()
			for row in rows:
				if row not in titles:
					titles.append(row)

		
		else:
			search = " "
		
		sidebar = utilities.getSideBar(email, user[9], cur)	
		print display("home.html").render(user=user,titles=titles,sidebar=sidebar,genre=genre,search=search)
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    print "Location: login.py?error=1"

if __name__ == '__main__':
	main()
