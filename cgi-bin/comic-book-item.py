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
	
	ISBN = form.getvalue('ISBN')
	code = form.getvalue('success')
	err = form.getvalue('error')

	try:
		cur = con.cursor()

		success = None
		error = None
		if code == '1':
			success = '<strong>Success: </strong> Comic Book successfully updated.'
		elif code == '2':
			success = '<strong>Success: </strong> Comic Book successfully created.'
		if err == '0':
			error = '<strong>Database Error:</strong> Foreign key constraint violated. Make sure to remove child records first.'

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie
		
		if email is None:
			print "Location: login.py?redirect=1\r\n"
		
		books = []
		command = "SELECT * from ComicBooks WHERE ISBN='" + ISBN + "'"
		cur.execute(command)
		book = cur.fetchone()
		for i in range(len(book)):
			books.append(book[i])

		awards = []
		command = "SELECT Award from LiteraryAwards WHERE ISBN='" + ISBN + "'"
		cur.execute(command)
		award = cur.fetchall()
		for i in range(len(award)):
			awards.append(award[i][0])
		books.append(awards)

		command = "SELECT WriterName from ComicBooks NATURAL JOIN BookWriter NATURAL JOIN Writers WHERE ISBN ='" + book[0] + "'"
		cur.execute(command)
		writers = cur.fetchall()

		command = "SELECT IllustratorName from ComicBooks NATURAL JOIN BookIllustrator NATURAL JOIN Illustrators WHERE ISBN ='" + book[0] + "'"
		cur.execute(command)
		illustrators= cur.fetchall()

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user = cur.fetchone()

		command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre WHERE ISBN ='" + book[0] + "'"
		cur.execute(command)
		genres = cur.fetchall()

		book_exists = False
		command = "SELECT * FROM UserCart WHERE Email=%s AND ISBN=%s"
		cur = con.cursor()
		cur.execute(command, (email, ISBN))
		book_ = cur.fetchone()
		if (book_ != None):
			book_exists = True

		book_owned = False
		command = "SELECT 1 from ComicBooks NATURAL JOIN UserOwned WHERE Email=%s AND ISBN=%s"
		cur = con.cursor()
                cur.execute(command, (email, ISBN))
                book_ = cur.fetchone()
                if (book_ != None):
                        book_owned = True
        
		
		sidebar = utilities.getSideBar(email,user[9], cur)
		print display("comic-book-item.html").render(error=error,success=success,book=books,user=user,sidebar=sidebar,writers=writers,illustrators=illustrators,genres=genres,book_exists=book_exists,book_owned=book_owned)
		sess.close()
		
	except mdb.Error, e:
	    if con:
	        con.rollback()
	    print "Location: login.py?error=1"

if __name__ == '__main__':
	main()
