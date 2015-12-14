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
	book = form.getvalue('ISBN')

	try:
		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie

		if email is None:
			print "Location: login.py?redirect=1\r\n"

		# Checks if book already exists in cart
		command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
		cur = con.cursor()
		cur.execute(command, (email, book))
		book_ = cur.fetchone()

		# Insert book into user's cart
		if book_ == None:
			command = "INSERT INTO UserCart(Email, ISBN) VALUES(%s, %s)"
			cur = con.cursor()
			cur.execute(command, (email, book))
		# Increment quantity
		else :
			command = "UPDATE UserCart SET Quantity = Quantity + 1 WHERE Email = '" + email + "' AND ISBN = " + book
			cur.execute(command)		
	
		#update total price
		command = "SELECT TotalCost from Users WHERE Email='" + email + "'"
		cur.execute(command)
		row = cur.fetchone()
		total = row[0]

		if total == None:
			total = 0

		command = "SELECT Price from ComicBooks WHERE ISBN='" + book + "'"
		cur.execute(command)
		row = cur.fetchone()
		price = row[0]

		total = total + price

		command = "UPDATE Users SET TotalCost='" + str(total) + "' WHERE Email='" + email + "'"
		cur.execute(command)
		con.commit()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user = cur.fetchone() 

		#Get titles of ComicBooks in cart
		command = "SELECT ISBN, Title, Price, Format, Quantity, Stock from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles_temp = []
		for row in rows:
			titles_temp.append(row)

		titles = []
		total = 0
		for title in titles_temp:
			#command = "SELECT WriterName from ComicBooks NATURAL JOIN BookWriter NATURAL JOIN Writers WHERE ISBN='" + title[0] + "'"
			#cur.execute(command)
			#row = cur.fetchone()

			new_title = title # + (row)
			titles.append(new_title)

		command = "SELECT TotalCost from Users WHERE Email='" + email + "'"
		cur.execute(command)
		row = cur.fetchone()
		total = row[0]

		sidebar = utilities.getSideBar(email,user[9], cur)
		print display("shopping-cart.html").render(sidebar=sidebar,user=user,titles=titles,total=total)
		print format
		sess.close()

	except mdb.Error, e:
		if con:
			con.rollback()

if __name__ == '__main__':
	main()
