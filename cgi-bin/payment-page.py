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
	deliveryaddress = form.getvalue("deliveryaddress")

	try:
		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie

		f = open("temp", "w")		

		if email is None:
			print "Location: login.py?redirect=1\r\n"
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone()

		# Create order record and retrieve its OrderID
		command = "INSERT INTO Orders(OrderDate, CustomerEmail, DeliveryAddress, Status) VALUES( NOW(), '" + email + "','" + deliveryaddress + "','Paid')"
		#f.write(command)
		cur.execute(command)
		command = "SELECT max(OrderID) FROM Orders where CustomerEmail ='" + email + "'"
		cur.execute(command)
		orderID = cur.fetchone()[0]
  
		# Retrieve books in User Cart
		command = "SELECT ISBN, Quantity from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"
		cur.execute(command)
		rows = cur.fetchall()
		#bookorders = []
		#for row in rows:
			#bookorders.append(row)


		# Add Book to Order
		for book in rows:	
			command = "INSERT INTO BookOrder(ISBN,OrderID,Quantity) values(" + book[0] + "," + str(orderID) + "," + str(book[1]) + ")"
			f.write(command + '\n')
			cur.execute(command)

		# Empty User Cart
		command = "DELETE FROM UserCart WHERE Email='" + email + "'"
		cur.execute(command)
		f.write(command + '\n')
		con.commit()
		

		#for isbn in ISBN_set:
		#	command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
		#	cur = con.cursor()
		#	cur.execute(command, (email, isbn))
		#	book_ = cur.fetchone()

			# Delete book from user's cart
		#	if book_ != None:
		#		command = "DELETE FROM UserCart WHERE Email=%s AND ISBN=%s"
		#		cur = con.cursor()
		#		cur.execute(command, (email, isbn))
 

			# Checks if book already exists in owned
			#command = "SELECT * FROM UserOwned WHERE Email=%s AND ISBN=%s"
			#cur = con.cursor()
			#cur.execute(command, (email, isbn))
			#book_ = cur.fetchone()

			#Insert book into user's cart
			#if book_ == None:
				#command = "INSERT INTO UserOwned(Email, ISBN) VALUES(%s, %s)"
				#cur = con.cursor()
				#cur.execute(command, (email, isbn))
		
		sidebar = utilities.getSideBar(email,user_[9], cur)
		print display("success.html").render(sidebar=sidebar,user=user_)
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
