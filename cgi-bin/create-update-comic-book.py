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
	action = form.getvalue('action')
	desc = form.getvalue('desc')
	format = form.getvalue('format')
	length = form.getvalue('length')
	publisher = form.getvalue('publisher')
	datepub = form.getvalue('datepub')
	price = form.getvalue('price')
	awards = form.getvalue('awards')
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
                user= cur.fetchone()

		if action == None :
			bookform = []
			if isbn != None :
				bookform = []
				command = "SELECT * FROM  ComicBooks where ISBN='" + isbn + "'";
				cur.execute(command)
				book = cur.fetchone()
				for i in book:
					bookform.append(i)

				awards = []
				command = "SELECT Award from LiteraryAwards WHERE ISBN='" + isbn + "'"
				cur.execute(command)
				award = cur.fetchall()
				for i in range(len(award)):
					awards.append(award[i][0])
				bookform.append(awards)

				command = "SELECT WriterName from BookWriter WHERE ISBN='" + isbn + "'"
				cur.execute(command)
				rows = cur.fetchall()

				writers_= []
				for row in rows:
					writers_.append(row[0])
				writers = utilities.getWriters(writers_, cur)

				command = "SELECT IllustratorName from BookIllustrator WHERE ISBN='" + isbn + "'"
				cur.execute(command)
				rows = cur.fetchall()

				illustrators_= []
				for row in rows:
					illustrators_.append(row[0])
				illustrators = utilities.getIllustrators(illustrators_, cur)

				command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre WHERE ISBN ='" + book[0] + "'"
				cur.execute(command)
				rows = cur.fetchall()
				genres_= []
				for row in rows:
					genres_.append(row[0])
				genres = utilities.getGenres(genres_, cur)

			else :
				writers = utilities.getWriters([], cur)	
				illustrators = utilities.getIllustrators([], cur)
				genres = utilities.getGenres([], cur)

			sidebar = utilities.getSideBar(email, user[9], cur)
			print display("comic-book-create-update.html").render(user=user,sidebar=sidebar,book=isbn,bookform=bookform,genres=genres,writers=writers,illustrators=illustrators)
			return

		else:
			# Update book attributes
			if isbn != None :
				update_command = "UPDATE ComicBooks SET "
				
				if bookdesc == None:
					update_command = update_command + " Description = NULL "
				else :
					update_command = update_command + " Description = '" + desc + "' "
				
				update_command =  update_command + " WHERE ISBN = '" + isbn +  "'"
				cur.execute(update_command)
				

				command = "DELETE FROM ComicBooks WHERE ISBN = '"  + isbn + "'"
				cur.execute(command)
				command = "SELECT * from ComicBooks WHERE ISBN ='" + isbn + "'"
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
					writers = utilities.getWriters([], cur)
					error = "Comic book " + create + " already exists! Provide another comic book."
					sidebar = utilities.getSideBar(email, user[9], cur)
					print display("comic-book-create-update.html").render(user=user,sidebar=sidebar,book=book,bookform=bookform,writers=writers,error=error)
				else :
					insert_command = "INSERT INTO ComicBooks(ISBN, Description) VALUES ('" + create + "','" + desc + "') \
										"
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
