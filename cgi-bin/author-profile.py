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
	
	author= form.getvalue('author') 
	email = form.getvalue('email') #email of current user

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() #

		command = "SELECT * from Authors WHERE AuthorId ='" + author + "'"
		cur.execute(command)
		author_ = cur.fetchone()

		command = "SELECT ISBN, Title, Price, Publisher, Description, Image, DatePublished, Format, Length from Books NATURAL JOIN BookAuthor NATURAL JOIN Authors WHERE AuthorId='" + author + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		command = "SELECT Genre from Books NATURAL JOIN BookGenre NATURAL JOIN BookAuthor WHERE AuthorId ='" + author + "'"
		cur.execute(command)
		genres = cur.fetchall()
		genres_ = []
		for genre in genres:
			if genre not in genres_:
				genres_.append(genre)

		print display("author-profile.html").render(user=user_,author=author_,titles=titles,genres=genres_)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()