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
	
	writer= form.getvalue('writer') 
	#email = form.getvalue('email') #email of current user
	action = form.getvalue('action') # action 

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

		if action != 'create' :
			command = "SELECT * from Writers WHERE WriterName='" + writer + "'"
			cur.execute(command)
			writer_ = cur.fetchone()

			command = "SELECT ISBN, Title, Price, Image from ComicBooks NATURAL JOIN BookWriter NATURAL JOIN Writers WHERE WriterName='" + writer + "'"
		
			cur.execute(command)
			rows = cur.fetchall()
			titles = []
			for row in rows:
				titles.append(row)

			command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre NATURAL JOIN BookWriter WHERE WriterName='" + writer + "'"
			cur.execute(command)
			genres = cur.fetchall()
			genres_ = []
			for genre in genres:
				if genre not in genres_:
					genres_.append(genre)

		sidebar = utilities.getSideBar(email, user_[9], cur)
		if action == 'create' :
			countryDropDown = utilities.generateCountryDropDown(None)
			bookitems = utilities.getBookItems([], cur)
			print display("writer-profile-create.html").render(user=user_,createform=None,sidebar=sidebar,bookitems=bookitems,countryDropDown=countryDropDown)
		else :
			print display("writer-profile.html").render(sidebar=sidebar,user=user_,writer=writer_,titles=titles,genres=genres_)
		sess.close()
		
	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
