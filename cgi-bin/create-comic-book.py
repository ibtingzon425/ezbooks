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
	action = form.getvalue('action')
	isbn = form.getvalue('ISBN')
	title = form.getvalue('title')
	desc = form.getvalue('desc')
	format = form.getvalue('format')
	length = form.getvalue('length')
	publisher = form.getvalue('publisher')
	datepub = form.getvalue('datepub')
	price = form.getvalue('price')
	awards = form.getvalue('awards')
	genres = form.getlist('genres')
	illustrators= form.getlist('illustrators')
	writers= form.getlist('writers')
	stock = form.getvalue('stock')

	try:
		state = "create"
		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie

		if desc != None:
			desc = desc.replace("\r\n", '<br>')
		
		if email is None:
			print "Location: login.py?redirect=1\r\n"

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
                cur.execute(command)
                user= cur.fetchone()


		if action == "create":
			bookform = []
			writers = utilities.getWriters([], cur)	
			illustrators = utilities.getIllustrators([], cur)
			genres = utilities.getGenres([], cur)

			sidebar = utilities.getSideBar(email, user[9], cur)
			print display("comic-book-create-update.html").render(state=state,user=user,sidebar=sidebar,bookform=bookform,genres=genres,writers=writers,illustrators=illustrators)
			return

			sidebar = utilities.getSideBar(email, user[9], cur)
			print display("comic-book-create-update.html").render(user=user,sidebar=sidebar,bookform=bookform,genres=genres,writers=writers,illustrators=illustrators)
			return

		elif action == "save":
			if isbn != None :
				command = "SELECT ISBN from ComicBooks where ISBN = '" + isbn + "'"
				cur.execute(command)
				bookRecord = cur.fetchone()

				if bookRecord is not None:
					bookform = []
					bookform.append(isbn)
					bookform.append(title)
					bookform.append(price)
					bookform.append(publisher)
					bookform.append(desc)
					bookform.append(" ")
					bookform.append(datepub)
					bookform.append(length)
					bookform.append(format)
					writers_= []
					for writer in writers:
						writers_.append(writer)
					writers = utilities.getWriters(writers_, cur)
					illustrators_= []
					for illustrator in illustrators:
						illustrators_.append(illustrator)
					illustrators = utilities.getIllustrators(illustrators_, cur)
					genres_= []
					for genre in genres:
						genres_.append(genre)
					genres = utilities.getGenres(genres_, cur)
					sidebar = utilities.getSideBar(email, user[9], cur)
					error = "Comic book " + isbn + " already exists! Provide another comic book."

					print display("comic-book-create-update.html").render(state="create",user=user,sidebar=sidebar,bookform=bookform,genres=genres,writers=writers,illustrators=illustrators,error=error)
				else :

					insert_command = "INSERT INTO ComicBooks(ISBN, Description, Title, Price, Publisher, DatePublished, Length, Format, Stock) VALUES"
					insert_command = insert_command + "(" 
					insert_command = insert_command + "'" + isbn + "'," 
					insert_command = insert_command + """ " """ + desc + """ " """ + ", '" + title + "','" + price + "','" + publisher + "','" + datepub + "','" + length + "','" + format + "','" + stock + "')"

					cur.execute(insert_command)	

					# upload image is user specified					
					if form.has_key('image_file'):
						update_command = "UPDATE ComicBooks SET "
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
								update_command = update_command + "Image = '" + "model/images/cover-" + isbn + extension  + "' "
								update_command =  update_command + " WHERE ISBN = '" + isbn +  "'"
								cur.execute(update_command)

					if awards != None:
						awards = awards.split(',')
						for award in awards:
							insert_command = "INSERT INTO LiteraryAwards(ISBN, Award) VALUES "
							insert_command =  insert_command + "( '" + isbn + """' , " """ + award + """ ")"""
							cur.execute(insert_command)
					
					if genres is not None:
						for genre in genres:
							insert_command = "INSERT INTO BookGenre(ISBN, Genre) VALUES "
							insert_command =  insert_command + "( '" + isbn + "' , '" + genre + "')"
							cur.execute(insert_command)
					
					if illustrators is not None:
						for illustrator in illustrators:
							insert_command = "INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES "
							insert_command =  insert_command + "( '" + isbn + "' , '" + illustrator + "')"
							cur.execute(insert_command)

					if writers is not None:
						for writer in writers:
							insert_command = "INSERT INTO BookWriter(ISBN, WriterName) VALUES "
							insert_command =  insert_command + "( '" + isbn + "' , '" + writer + "')"
							cur.execute(insert_command)
					
					con.commit() 

					print "Location: comic-book-item.py?ISBN=" + isbn + "&success=2\r\n"
					

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    invaidPageError()


	    

if __name__ == '__main__':
	main()
