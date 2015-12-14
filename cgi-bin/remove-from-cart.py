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
	email = form.getvalue('email') #email of current user
	book = form.getvalue('ISBN')
	action = form.getvalue('action')
	total = 0.0

	try:
		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie

		# Checks if book already exists in cart
		command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
		cur = con.cursor()
		cur.execute(command, (email, book))
		book_ = cur.fetchone()

		if email is None:
			print "Location: login.py?redirect=1\r\n"

		#Delete book into user's cart
		if book_ != None:
			if action == 'subtract' :
				quantity = 1
				command = "UPDATE UserCart SET Quantity = Quantity - 1 WHERE Email=%s AND ISBN=%s"
			else :
				# Check quantity first
				command = "SELECT QUANTITY FROM UserCart WHERE Email=%s AND ISBN=%s"
				cur.execute(command, (email, book))
				row = cur.fetchone()
				quantity = row[0]

				command = "DELETE FROM UserCart WHERE Email=%s AND ISBN=%s"
			cur = con.cursor()
			cur.execute(command, (email, book))

			command = "SELECT TotalCost from Users WHERE Email='" + email + "'"
			cur.execute(command)
			row = cur.fetchone()
			total = row[0]

			command = "SELECT Price from ComicBooks WHERE ISBN='" + book + "'"
			cur.execute(command)
			row = cur.fetchone()
			price = row[0]

			if (total >= price):
				total = total - (price*quantity)
			else:
				total = 0

			command = "UPDATE Users SET TotalCost=%s WHERE Email=%s"
			cur.execute(command, (total, email))
			con.commit()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() 

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

			new_title = title #+ (row)
			titles.append(new_title)


		command = "SELECT TotalCost from Users WHERE Email='" + email + "'"
		cur.execute(command)
		row = cur.fetchone()
		total = row[0]

		
		sidebar = utilities.getSideBar(email,user[9], cur)
		print display("shopping-cart.html").render(sidebar=sidebar,user=user,titles=titles,total=total)
		sess.close()
	except mdb.Error, e:
		if con:
			con.rollback()

if __name__ == '__main__':
	main()
