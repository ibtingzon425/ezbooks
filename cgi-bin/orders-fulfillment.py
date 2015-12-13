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
	action = form.getvalue('action') # action 
	order = form.getvalue('order')

	success = None
	error = None

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
		user = cur.fetchone() #
		
		if action == 'ship' :
			command = "UPDATE Orders SET Status = 'Shipped' WHERE OrderID = " + order
			cur.execute(command)
			con.commit()
			success = "<strong>Success: </strong> Order with Order ID " + order + " has been marked as Shipped."
		elif action == 'deliver' :
			command = "UPDATE Orders SET Status = 'Delivered' WHERE OrderID = " + order
			cur.execute(command)
			con.commit()
			success = "<strong>Success: </strong> Order with Order ID " + order + " has been marked as Delivered."
		elif action == 'cancel' :
			command = "UPDATE Orders SET Status = 'Canceled' WHERE OrderID = " + order
			cur.execute(command)
			con.commit() 
			success = "<strong>Success: </strong> Order with Order ID " + order + " has been Canceled."

		# Retrieve Paid Orders
		command = "SELECT o.OrderID, OrderDate, Quantity, cb.ISBN, cb.Title, DeliveryAddress, o.CustomerEmail, u.FirstName, u.LastName " + \
			  "FROM Orders o, BookOrder bo, ComicBooks cb, Users u " + \
		          "WHERE o.OrderID = bo.OrderID " + \
  		          "  AND bo.ISBN = cb.ISBN " + \
  		          "  AND o.Status in ('Paid') " + \
			  "  AND u.Email = o.CustomerEmail " + \
		          "ORDER BY OrderDate"
		cur.execute(command)
		rows = cur.fetchall()
		paidOrders = []
		i=0
		while i < len(rows) :
			j = i + 1
			userHTML = '<a href="user-profile.py?user=' + rows[i][6] + '">' + rows[i][7] + ' ' +  rows[i][8] + \
				   '</a>'
			bookHTML = str(rows[i][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[i][3]) + '">' + str(rows[i][4]) + \
				   ' (' +str(rows[i][3]) +  ')</a>'
			while j < len(rows) and (rows[i][0]==rows[j][0]):
				bookHTML = bookHTML + '<br/>' + str(rows[j][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[j][3]) + '">' + \
					   str(rows[j][4]) + ' (' +str(rows[i][3]) +  ')</a>'
				j = j + 1
			paidOrders.append( [rows[i][0], rows[i][1], bookHTML, rows[i][5], userHTML] )
			i = j

		# Retrieve Shipped Orders
                command = "SELECT o.OrderID, OrderDate, Quantity, cb.ISBN, cb.Title, DeliveryAddress, o.CustomerEmail, u.FirstName, u.LastName " + \
                          "FROM Orders o, BookOrder bo, ComicBooks cb, Users u " + \
                          "WHERE o.OrderID = bo.OrderID " + \
                          "  AND bo.ISBN = cb.ISBN " + \
                          "  AND o.Status in ('Shipped') " + \
                          "  AND u.Email = o.CustomerEmail " + \
                          "ORDER BY OrderDate"
                cur.execute(command)
                rows = cur.fetchall()
                shippedOrders = []
                i=0
                while i < len(rows) :
                        j = i + 1
                        userHTML = '<a href="user-profile.py?user=' + rows[i][6] + '">' + rows[i][7] + ' ' +  rows[i][8] + \
                                   '</a>'
                        bookHTML = str(rows[i][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[i][3]) + '">' + str(rows[i][4]) + \
                                   ' (' +str(rows[i][3]) +  ')</a>'
                        while j < len(rows) and (rows[i][0]==rows[j][0]):
                                bookHTML = bookHTML + '<br/>' + str(rows[j][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[j][3]) + '">' + \
                                           str(rows[j][4]) + ' (' +str(rows[i][3]) +  ')</a>'
                                j = j + 1
                        shippedOrders.append( [rows[i][0], rows[i][1], bookHTML, rows[i][5], userHTML] )
                        i = j

		sidebar = utilities.getSideBar(email,user[9], cur)
		print display("orders-fulfillment.html").render(user=user,sidebar=sidebar,paidOrders=paidOrders,shippedOrders=shippedOrders,success=success,error=error)	
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
