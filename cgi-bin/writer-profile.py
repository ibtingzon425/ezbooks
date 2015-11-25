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
	
	writer= form.getvalue('writer') 
	email = form.getvalue('email') #email of current user

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() #

		command = "SELECT * from Writers WHERE WriterId ='" + writer + "'"
		cur.execute(command)
		writer_ = cur.fetchone()

		command = "SELECT ISBN, Title, Price, Image from ComicBooks NATURAL JOIN BookWriter NATURAL JOIN Writers WHERE WriterId='" + writer + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre NATURAL JOIN BookWriter WHERE WriterId ='" + writer + "'"
		cur.execute(command)
		genres = cur.fetchall()
		genres_ = []
		for genre in genres:
			if genre not in genres_:
				genres_.append(genre)

		sidebar = utilities.getSideBar(email, user_[9], cur)
		print display("writer-profile.html").render(sidebar=sidebar,user=user_,writer=writer_,titles=titles,genres=genres_)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
