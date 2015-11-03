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

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() #

		command = "SELECT ISBN, Title, Price, Format from Books NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles_temp = []
		for row in rows:
			titles_temp.append(row)

		titles = []
		total = 0
		for title in titles_temp:
			command = "SELECT AuthorName, AuthorId from Books NATURAL JOIN BookAuthor NATURAL JOIN Authors WHERE ISBN='" + title[0] + "'"
			cur.execute(command)
			row = cur.fetchone()
			new_title = title + (row)
			titles.append(new_title)
			total = total + title[2]

		command = "UPDATE Users SET TotalCost='" + str(total) + "' WHERE Email='" + email + "'"
		cur.execute(command)
		con.commit()

		print display("shopping-cart.html").render(user=user_,titles=titles,total=total)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()