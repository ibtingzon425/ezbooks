#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie, json
import utilities

def invaidPageError():
	print "<script type='text/javascript'> \
	          alert('Error occurred. Please try again.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	
	#email = form.getvalue('email')
	book = form.getvalue('book')
	action = form.getvalue('action')
	desc = form.getvalue('desc')
	create = form.getvalue('create')
	isbn = form.getlist('isbn')

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

		if action == None :
			if book != None :
				command = "SELECT * FROM  ComicBooks where ISBN='" + isbn + "'";
				cur.execute(command)
				bookform = cur.fetchone()

				# Get books associated with book
				command = "SELECT ISBN from ComicBooks WHERE ISBN='" + isbn + "' order by Title"
				cur.execute(command)
				rows = cur.fetchall()

				titles = []
				for row in rows:
					titles.append(row[0])

				bookitems = utilities.getBookItems(titles, cur)
			else :
				bookform = None
        			bookitems = utilities.getBookItems([], cur)	

			sidebar = utilities.getSideBar(email, user[9], cur)
			print display("comic-book-create-update.html").render(user=user,sidebar=sidebar,book=book,bookform=bookform,bookitems=bookitems)
			return

		else :
			# Update
			if book != None :
				update_command = "UPDATE books SET "
				
				if bookdesc == None:
					update_command = update_command + " Description = NULL "
				else :
					update_command = update_command + " Description = '" +desc + "' "
				
				update_command =  update_command + " WHERE ISBN = '" + isbn +  "'"
				cur.execute(update_command)
				

				command = "DELETE FROM ComicBooks WHERE ISBN = '"  + isbn + "'"
				cur.execute(command)

				
                        	command = "SELECT * from ComicBooks NATURAL JOIN Bookbook WHERE ISBN ='" + isbn + "'"
                        	cur.execute(command)
                        	rows = cur.fetchall()
                        	titles = []
                        	for row in rows:
                                	titles.append(row)

                        	sidebar = utilities.getSideBar(email, user[9], cur)
                        	print display("home.html").render(user=user,titles=titles,sidebar=sidebar,book=book,bookdesc=bookdesc,search=' ')
			else :
				# Check if book exists
				command = "SELECT ISBN from ComicBooks where ISBN = '" + isbn + "'"
				cur.execute(command)
				bookRecord = cur.fetchone()

				if bookRecord is not None:
					bookform = []
					bookform.append(create)
					bookform.append(desc)
					sidebar = utilities.getSideBar(email, user[9], cur)
					bookitems = utilities.getBookItems(bookbooks, cur)
					error = "Comic book " + create + " already exists! Provide another comic book."
					sidebar = utilities.getSideBar(email, user[9], cur)
					print display("comic-book-create-update.html").render(user=user,sidebar=sidebar,book=book,bookform=bookform,bookitems=bookitems,error=error)
				else :
					insert_command = "INSERT INTO ComicBooks(ISBN, Description) VALUES ('" + create + "','" + desc + "') "
					cur.execute(insert_command)

					book = bookcreate 			 
					command = "SELECT * from ComicBooks  WHERE ISBN='" + isbn + "'"
                                	cur.execute(command)
                                	rows = cur.fetchall()
                                	titles = []
                                	for row in rows:
                                        	titles.append(row)

                                	sidebar = utilities.getSideBar(email, user[9], cur)
                                	print display("home.html").render(user=user,titles=titles,sidebar=sidebar,book=book,bookdesc=bookdesc,search=' ')			

	except mdb.Error, e:
	    if con:
	        con.rollback()

	    

if __name__ == '__main__':
	main()