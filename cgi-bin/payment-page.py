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
	
	#email = form.getvalue('email') #email of current user
	creditcard = form.getvalue("creditcard")

	try:
		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() 

		command = "SELECT ISBN from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		ISBN_set = []
		for row in rows:
			ISBN_set.append(row[0])

		for isbn in ISBN_set:
			command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
			cur = con.cursor()
			cur.execute(command, (email, isbn))
			book_ = cur.fetchone()

			#Delete book into user's cart
			if book_ != None:
				command = "DELETE FROM UserCart WHERE Email=%s AND ISBN=%s"
				cur = con.cursor()
				cur.execute(command, (email, isbn))
				con.commit()

			# Checks if book already exists in owned
			command = "SELECT * FROM UserOwned WHERE Email=%s AND ISBN=%s"
			cur = con.cursor()
			cur.execute(command, (email, isbn))
			book_ = cur.fetchone()

			#Insert book into user's cart
			if book_ == None:
				command = "INSERT INTO UserOwned(Email, ISBN) VALUES(%s, %s)"
				cur = con.cursor()
				cur.execute(command, (email, isbn))
				con.commit()

		
		sidebar = utilities.getSideBar(email,user_[9], cur)
		print display("success.html").render(sidebar=sidebar,user=user_)
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
