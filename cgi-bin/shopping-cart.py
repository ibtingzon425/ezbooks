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
		user_= cur.fetchone() #

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

			total = total + title[2]*title[4]

		command = "UPDATE Users SET TotalCost='" + str(total) + "' WHERE Email='" + email + "'"
		cur.execute(command)
		con.commit()

		sidebar = utilities.getSideBar(email, user_[9], cur)
		print display("shopping-cart.html").render(sidebar=sidebar,user=user_,titles=titles,total=total)
		sess.close()

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
