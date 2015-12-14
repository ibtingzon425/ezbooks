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
	
	userprof = form.getvalue('user') #email of userprofile
	userprofile = form.getvalue('user')
	#email = form.getvalue('email') #email of current user
	firstname = form.getvalue('first_name')
	lastname = form.getvalue('last_name')
	current_password = form.getvalue('current_password')
	new_password = form.getvalue('new_password')
	country = form.getvalue('country')
	birthdate = form.getvalue('birth_date')
	is_administrator = form.getvalue('is_administrator') 	

	#TODO: If current user != email 

	try:

		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie
		
		if email is None:
			print "Location: login.py?redirect=1\r\n"

		update_command = "UPDATE Users SET FirstName = '" + firstname + "', LastName = '" + lastname + "' "

		# check if password changed
		if current_password != new_password :
			enc_password = sha512_crypt.encrypt(new_password)
			update_command = update_command + ", Password = '" + enc_password + "' "

		# set country
		if country is None:
			update_command = update_command + ", Country = null "
		else :
			update_command = update_command + ", Country = '" + country + "' " 

		# set birth date
		if birthdate is None:
			update_command = update_command + ", Birthdate = null "
		else :
			update_command = update_command + ", Birthdate = '" + birthdate + "' "

		# upload image is user specified
 		if form.has_key('image_file'):
			
    			fileitem = form['image_file']
    			if fileitem.file :
				extension = os.path.splitext(fileitem.filename)[1] 
				if extension != '' :
					fout = file ("model/users/" +  userprof + extension , 'wb')
    					while 1:
        					chunk = fileitem.file.read(100000)
        					if not chunk: break
        					fout.write(chunk)
    					fout.close()
					update_command = update_command + ", Image = '" + "model/users/" +  userprof + extension  + "' "
		
		# set is administrator
		if is_administrator is not None:
			update_command = update_command + ", IsAdmin = '" + is_administrator + " '"

		update_command = update_command + "WHERE Email = '" + userprof + "'"
		cur.execute(update_command)
		con.commit() 
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() #

		command = "SELECT * FROM Users WHERE Email = '" + userprof + "'";
		cur.execute(command)
		userprof = cur.fetchone() #

		command = "SELECT * from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"
		
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
	
		sidebar = utilities.getSideBar(email,user[9], cur)
		successmsg = '<strong>Success:</strong> User Profile has been updated.'
		print display("user-profile.html").render(user=user,userprof=userprof,sidebar=sidebar,titles=titles,pendingOrders=pendingOrders,completedOrders=completedOrders,success=successmsg)
		sess.close()		
	
	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
