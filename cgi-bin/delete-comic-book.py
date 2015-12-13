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
	isbn = form.getvalue('ISBN')
	
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
		user = cur.fetchone()

		command = "DELETE FROM ComicBooks Where ISBN = '" + isbn +  "'";		
		cur.execute(command)
		con.commit()

		command = "SELECT * from ComicBooks"	
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)		

		sidebar = utilities.getSideBar(email, user[9], cur)
		successMsg = "<strong>Success:</strong> Comic Book '" + isbn + "' has been deleted."
		print display("home.html").render(user=user,titles=titles,sidebar=sidebar,search=' ',genre=None,publisher=None, success=successMsg)
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()

		sidebar = utilities.getSideBar(email, user[9], cur)
	    print "Location: comic-book-item.py?ISBN=" + isbn + "&error=0\r\n"
         
if __name__ == '__main__':
	main()
