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
	
	email = form.getvalue('email')
	genre = form.getvalue('genre')

	#TODO: For fname, lname == None redirect to login page
	#TODO: Implement sessions using Cookies
	
	try:
		cur = con.cursor()

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone()

		command = "DELETE FROM Genres Where Genre = '" + genre +  "'";		
		cur.execute(command)
		con.commit()

		command = "SELECT * from ComicBooks"	
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)
		

		sidebar = utilities.getSideBar(email, user[9], cur)
		successMsg = "Genre '" + genre + "' has been deleted."
		print display("home.html").render(user=user,titles=titles,sidebar=sidebar,search=' ',genre=None,publisher=None, success=successMsg)

	except mdb.Error, e:
	    if con:
	        con.rollback()

	    #file.write(e.args[1])
	    command = "SELECT * from ComicBooks NATURAL JOIN BookGenre WHERE Genre='" + genre + "'"
	    cur.execute(command)
            rows = cur.fetchall()
		
            titles = []
            for row in rows:
            	titles.append(row)

	    genre_ = [None, None]
	    command = "SELECT * FROM Genres WHERE Genre = '" + genre + "'";
	    cur.execute(command)
	    genre_ = cur.fetchone()

	    sidebar = utilities.getSideBar(email, user[9], cur)

            #print display("home.html").render(user=user,sidebar=sidebar,error=e.args[1])
	    if 'FOREIGN KEY' in e.args[1] :
		errMsg = 'Foreign key constraint violated. Make sure to remove child records first.'
	    else : 
	    	errMsg = e.args[1]
            print display("home.html").render(user=user,titles=titles,sidebar=sidebar,genre=genre_[0],genredesc=genre_[1],search=' ',publisher=None,error=errMsg)


if __name__ == '__main__':
	main()