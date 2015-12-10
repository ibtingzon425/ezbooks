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
	genre = form.getvalue('genre')
	action = form.getvalue('action')
	genredesc = form.getvalue('genredesc')
	genrecreate = form.getvalue('genrecreate')
	genrebooks = form.getlist('genrebooks')

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
			if genre != None :
				command = "SELECT * FROM Genres where Genre='" + genre + "'";
				cur.execute(command)
				genreform= cur.fetchone()

				# Get books associated with genre
				command = "SELECT ISBN from ComicBooks NATURAL JOIN BookGenre WHERE Genre='" + genre + "' order by Title"
				cur.execute(command)
				rows = cur.fetchall()		

				titles = []
				for row in rows:
					titles.append(row[0])

				bookitems = utilities.getBookItems(titles, cur)
			else :
				genreform = None
        			bookitems = utilities.getBookItems([], cur)	

			sidebar = utilities.getSideBar(email, user[9], cur)

			print display("genre-create-update.html").render(user=user,sidebar=sidebar,genre=genre,genreform=genreform,bookitems=bookitems)
			return

		else :
			# Update
			if genre != None :
				update_command = "UPDATE Genres SET "
				
				if genredesc == None:
					update_command = update_command + " GenreDesc = NULL "
				else :
					update_command = update_command + " GenreDesc = '" + genredesc + "' "
				
				update_command =  update_command + " WHERE Genre = '" + genre +  "'"
				cur.execute(update_command)
				

				command = "DELETE FROM BookGenre WHERE Genre = '"  + genre + "'"
				cur.execute(command)

				# Associate Books to Genre
                                for book in genrebooks:
                                	command = "INSERT INTO BookGenre(ISBN, Genre) VALUES (" + book + ",'"  + genre + "')"
                                        cur.execute(command)
                                con.commit()


                        	command = "SELECT * from ComicBooks NATURAL JOIN BookGenre WHERE Genre='" + genre + "'"
                        	cur.execute(command)
                        	rows = cur.fetchall()
                        	titles = []
                        	for row in rows:
                                	titles.append(row)

                        	sidebar = utilities.getSideBar(email, user[9], cur)
				success = '<strong>Success: </strong> Genre has been updated.'
                        	print display("home.html").render(user=user,titles=titles,sidebar=sidebar,genre=genre,genredesc=genredesc,search=' ',success=success)
			else :
				# Check if genre exists
				command = "SELECT Genre from Genres where Genre = '" + genrecreate + "'"
				cur.execute(command)
				genreRecord = cur.fetchone()

				if genreRecord is not None:
					genreform = []
					genreform.append(genrecreate)
					genreform.append(genredesc)
					sidebar = utilities.getSideBar(email, user[9], cur)
					bookitems = utilities.getBookItems(genrebooks, cur)
					error = "<strong>Database Error:</strong>  Genre " + genrecreate + " already exists! Provide another genre name."
					sidebar = utilities.getSideBar(email, user[9], cur)
					print display("genre-create-update.html").render(user=user,sidebar=sidebar,genre=genre,genreform=genreform,bookitems=bookitems,error=error)
				else :
					insert_command = "INSERT INTO Genres(Genre, GenreDesc) VALUES ('" + genrecreate + "','" + genredesc + "') "
					cur.execute(insert_command)

					# Associate Books to Genre
					for book in genrebooks:
						command = "INSERT INTO BookGenre(ISBN, Genre) VALUES (" + book + ",'"  + genrecreate + "')"
						cur.execute(command)
					con.commit()

					genre = genrecreate 			 
					command = "SELECT * from ComicBooks NATURAL JOIN BookGenre WHERE Genre='" + genre + "'"
                                	cur.execute(command)
                                	rows = cur.fetchall()
                                	titles = []
                                	for row in rows:
                                        	titles.append(row)

                                	sidebar = utilities.getSideBar(email, user[9], cur)
					success = '<strong>Success: </strong> Genre '  + genrecreate + ' has been created.'
                                	print display("home.html").render(user=user,titles=titles,sidebar=sidebar,genre=genre,genredesc=genredesc,search=' ',success=success)			

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    

if __name__ == '__main__':
	main()
