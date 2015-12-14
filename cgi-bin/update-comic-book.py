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
	title = form.getvalue('title')
	desc = form.getvalue('desc')
	format = form.getvalue('format')
	length = form.getvalue('length')
	publisher = form.getvalue('publisher')
	datepub = form.getvalue('datepub')
	price = form.getvalue('price')
	awards = form.getvalue('awards')
	isbn = form.getvalue('ISBN')
	genres = form.getlist('genres')
	illustrators= form.getlist('illustrators')
	writers= form.getlist('writers')
	stock = form.getvalue('stock')

	try:
		state = "update"
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

		if desc != None:
			desc = desc.replace('\r\n', '<br>')

		if action == "edit":
			bookform = []
			if isbn != None :
				bookform = []
				command = "SELECT * FROM  ComicBooks where ISBN='" + isbn + "'";
				cur.execute(command)
				book = cur.fetchone()
				for i in book:
					bookform.append(i)
				bookform[4] = bookform[4].strip() 

				awards = []
				command = "SELECT Award from LiteraryAwards WHERE ISBN='" + isbn + "'"
				cur.execute(command)
				award = cur.fetchall()
				for i in range(len(award)):
					award_ = award[i][0].strip()
					awards.append(award_)
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
			print display("comic-book-create-update.html").render(state=state,user=user,sidebar=sidebar,bookform=bookform,genres=genres,writers=writers,illustrators=illustrators)
			return

		elif action == "save":

			update_command = "UPDATE ComicBooks SET "
			
			update_command = update_command + " Format = '" + format + "' "
			update_command = update_command + ", Title = '" + title + "' "
			update_command = update_command + ", Length = '" + length + "' "
			update_command = update_command + ", Publisher = '" + publisher + "' "
			update_command = update_command + ", DatePublished = '" + datepub + "' "
			update_command = update_command + ", Price = '" + price + "' "
			update_command = update_command + ", Stock = '" + stock + "' "

			if desc is None:
				 update_command = update_command + ", Description = null "
			else :
				update_command = update_command + """, Description = " """ + desc + """ " """	

			# upload image is user specified
			if form.has_key('image_file'):
				fileitem = form['image_file']
				if fileitem.file:
					extension = os.path.splitext(fileitem.filename)[1] 
					if extension != '' :
						fout = file ("model/images/cover-" +  isbn + extension , 'wb')
						while 1:
							chunk = fileitem.file.read(100000)
							if not chunk: 
								break
							fout.write(chunk)
						fout.close()
						update_command = update_command + ", Image = '" + "model/images/cover-" + isbn + extension  + "' "

			update_command =  update_command + " WHERE ISBN = '" + isbn +  "'"
			cur.execute(update_command)

			command = "DELETE FROM LiteraryAwards Where ISBN = '" + isbn +  "'";
			cur.execute(command)
			
			if awards != None:
				awards = awards.split(',')
				for award in awards:
					insert_command = "INSERT INTO LiteraryAwards(ISBN, Award) VALUES "
					insert_command =  insert_command + "( '" + isbn + """' , " """ + award + """ ")"""
					cur.execute(insert_command)
					con.commit() 

			command = "DELETE FROM BookGenre Where ISBN = '" + isbn +  "'";		
			cur.execute(command)
			con.commit()
			
			if genres is not None:
				for genre in genres:
					insert_command = "INSERT INTO BookGenre(ISBN, Genre) VALUES "
					insert_command =  insert_command + "( '" + isbn + "' , '" + genre + "')"
					cur.execute(insert_command)

			command = "DELETE FROM BookIllustrator Where ISBN = '" + isbn +  "'";		
			cur.execute(command)
			
			if illustrators is not None:
				for illustrator in illustrators:
					insert_command = "INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES "
					insert_command =  insert_command + "( '" + isbn + "' , '" + illustrator + "')"
					cur.execute(insert_command)

			command = "DELETE FROM BookWriter Where ISBN = '" + isbn +  "'";		
			cur.execute(command)
			
			if writers is not None:
				for writer in writers:
					insert_command = "INSERT INTO BookWriter(ISBN, WriterName) VALUES "
					insert_command =  insert_command + "( '" + isbn + "' , '" + writer + "')"
					cur.execute(insert_command)
			con.commit() 
			
			print "Location: comic-book-item.py?ISBN=" + isbn + "&success=1\r\n"
			
	except mdb.Error, e:
	    if con:
	        con.rollback()

	    

if __name__ == '__main__':
	main()
