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
		if book_ == None:
			command = "INSERT INTO UserCart(Email, ISBN) VALUES(%s, %s)"
			cur = con.cursor()
			cur.execute(command, (email, book))
			con.commit()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() 

		#Get titles of books in cart
		command = "SELECT ISBN, Title, Price, Format from Books NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles_temp = []
		for row in rows:
			titles_temp.append(row)

		titles = []
		for title in titles_temp:
			command = "SELECT AuthorName, AuthorId from Books NATURAL JOIN BookAuthor NATURAL JOIN Authors WHERE ISBN='" + title[0] + "'"
			cur.execute(command)
			row = cur.fetchone()
			new_title = title + (row)
			titles.append(new_title)

		#update total price
		command = "SELECT TotalCost from Users WHERE Email='" + email + "'"
		cur.execute(command)
		row = cur.fetchone()
		total = row[0]

		command = "SELECT Price from Books WHERE ISBN='" + book + "'"
		cur.execute(command)
		row = cur.fetchone()
		price = row[0]

		total = total + price

		command = "UPDATE Users SET TotalCost='" + str(total) + "' WHERE Email='" + email + "'"
		cur.execute(command)
		con.commit()

		#print display("user-profile.html").render(user=user,userprof=user,titles=titles)
		print display("shopping-cart.html").render(user=user,titles=titles,total=total)

	except mdb.Error, e:
		if con:
			con.rollback()

if __name__ == '__main__':
	main()