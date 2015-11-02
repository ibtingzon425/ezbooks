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
	book = form.getvalue('ISBN')

	try:
		# Checks if book already exists in cart
		command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
		cur = con.cursor()
		cur.execute(command, (email, book))
		book_ = cur.fetchone()

		#Insert book into user's cart
		if book_ != None:
			command = "DELETE FROM UserCart WHERE Email=%s AND ISBN=%s"
			cur = con.cursor()
			cur.execute(command, (email, book))
			con.commit()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() 

		command = "SELECT ISBN, Title, Price, Publisher, Description, Image from Books NATURAL JOIN UserCart NATURAL JOIN Users WHERE Email='" + email + "'"
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		print display("user-profile.html").render(user=user,userprof=user,titles=titles)

	except mdb.Error, e:
		if con:
			con.rollback()

if __name__ == '__main__':
	main()