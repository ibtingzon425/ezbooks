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
	
	illustrator= form.getvalue('illustrator') 
	#email = form.getvalue('email') #email of current user

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
		user_= cur.fetchone() #

		command = "SELECT * from Illustrators WHERE IllustratorName ='" + illustrator + "'"
		cur.execute(command)
		illustrator_ = cur.fetchone()

		command = "SELECT ISBN, Title, Price, Image from ComicBooks NATURAL JOIN BookIllustrator NATURAL JOIN Illustrators WHERE IllustratorName='" + illustrator + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre NATURAL JOIN BookIllustrator WHERE IllustratorName ='" + illustrator + "'"
		cur.execute(command)
		genres = cur.fetchall()
		genres_ = []
		for genre in genres:
			if genre not in genres_:
				genres_.append(genre)

		sidebar = utilities.getSideBar(email,user_[9], cur)
		print display("illustrator-profile.html").render(sidebar=sidebar,user=user_,illustrator=illustrator_,titles=titles,genres=genres_)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
