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
	
	#email = form.getvalue('email')
	userprofile = form.getvalue('user')

	#TODO: For fname, lname == None redirect to login page
	#TODO: Implement sessions using Cookies
	
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
		user= cur.fetchone()

		command = "DELETE FROM Users Where Email = '" + userprofile +  "'";		
		cur.execute(command)
		con.commit()

		command = "SELECT * from ComicBooks"	
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)
		

		sidebar = utilities.getSideBar(email, user[9], cur)
		successMsg = "<strong>Success:</strong> User with email '" + userprofile + "' has been deleted."
		print display("home.html").render(user=user,titles=titles,sidebar=sidebar,search=' ',genre=None,publisher=None, success=successMsg)

	except mdb.Error, e:
	    if con:
	        con.rollback()

	    command = "SELECT * FROM Users WHERE Email = '" + userprofile + "'";
	    cur.execute(command)
	    userprof = cur.fetchone() #

	    command = "SELECT * from ComicBooks NATURAL JOIN UserCart WHERE Email='" + userprofile + "'"
            cur.execute(command)
            rows = cur.fetchall()
	    titles = []
	    for row in rows:
		titles.append(row)

	    # Retrieve Pending Orders
            command = "SELECT o.OrderID, OrderDate, Quantity, cb.ISBN, cb.Title, DeliveryAddress, Status " + \
                      "FROM Orders o, BookOrder bo, ComicBooks cb " + \
                      "WHERE o.OrderID = bo.OrderID " + \
                      "  AND bo.ISBN = cb.ISBN " + \
                      "  AND o.Status in ('Paid', 'Shipped') " + \
                      "  AND o.CustomerEmail = '" + userprofile + "' " + \
                      "ORDER BY OrderDate DESC"
            cur.execute(command)
            rows = cur.fetchall()
            pendingOrders = []
            i=0
            while i < len(rows) :
            	j = i + 1
                bookHTML = str(rows[i][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[i][3]) + '">' + str(rows[i][4]) + \
                           ' (' +str(rows[i][3]) +  ')</a>'
                while j < len(rows) and (rows[i][0]==rows[j][0]):
                	bookHTML = bookHTML + '<br/>' + str(rows[j][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[j][3]) + '">' + \
                                   str(rows[j][4]) + ' (' +str(rows[j][3]) +  ')</a>'
                        j = j + 1
                        pendingOrders.append( [rows[i][0], rows[i][1], bookHTML, rows[i][5], rows[i][6]] )
                i = j

	    # Retrieve 3 Latest Completed Orders
            command = "SELECT o.OrderID, OrderDate, Quantity, cb.ISBN, cb.Title, DeliveryAddress, Status " + \
                      "FROM BookOrder bo, ComicBooks cb, " + \
                      "(SELECT OrderID, OrderDate, DeliveryAddress, Status " + \
                       "FROM Orders WHERE Status in ('Delivered', 'Canceled') AND CustomerEmail = '" + userprofile + "' " + \
                       "ORDER BY OrderDate DESC LIMIT 3) o " + \
                       "WHERE o.OrderID = bo.OrderID AND bo.ISBN = cb.ISBN"
            cur.execute(command)
            rows = cur.fetchall()
            completedOrders = []
            i=0
            while i < len(rows) :
            	j = i + 1
                bookHTML = str(rows[i][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[i][3]) + '">' + str(rows[i][4]) + \
                           ' (' +str(rows[i][3]) +  ')</a>'
                while j < len(rows) and (rows[i][0]==rows[j][0]):
                	bookHTML = bookHTML + '<br/>' + str(rows[j][2]) + ' X <a href="comic-book-item.py?ISBN=' + str(rows[j][3]) + '">' + \
                                   str(rows[j][4]) + ' (' +str(rows[j][3]) +  ')</a>'
                        j = j + 1
                completedOrders.append( [rows[i][0], rows[i][1], bookHTML, rows[i][5], rows[i][6]] )
                i = j

	    sidebar = utilities.getSideBar(email, user[9], cur)

            #print display("home.html").render(user=user,sidebar=sidebar,error=e.args[1])
	    if 'FOREIGN KEY' in e.args[1] :
		errMsg = '<strong>Database Error:</strong> Foreign key constraint violated. Make sure to remove child records first.'
	    else : 
	    	errMsg = e.args[1]
            print display("user-profile.html").render(user=user,userprof=userprof,sidebar=sidebar,titles=titles,pendingOrders=pendingOrders,completedOrders=completedOrders,error=errMsg)
        sess.close()

if __name__ == '__main__':
	main()
