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
	
	userprof = form.getvalue('user') #email of userprofile
	#email = form.getvalue('email') #email of current user
	name = form.getvalue('name')
	born = form.getvalue('country')
	birthdate = form.getvalue('birth_date')
	gender = form.getvalue('gender') 	
	description = form.getvalue('desc')
	illustratorbooks = form.getlist('illustratorbooks')
	#TODO: If current user != email 
	
	try:

		cur = con.cursor()

		sess = session.Session(expires=365*24*60*60, cookie_path='/')
		lastvisit = sess.data.get('lastvisit')
		email= sess.data.get('user')
		print sess.cookie
		
		if email is None:
			print "Location: login.py?redirect=1\r\n"

		if description != None:
			description = description.replace('\r\n', '<br>')

		update_command = "UPDATE Illustrators SET "

		# set gender
		update_command = update_command +  " Gender = '" + gender + "' "

		# set description
		if description is None:
			 update_command = update_command + ", IllustratorDescription = null "
		else :
			 update_command = update_command + ", IllustratorDescription = '" + description + "' "
				

		# set country
		if born is None:
			update_command = update_command + ", Born = null "
		else :
			update_command = update_command + ", Born = '" + born + "' " 

		# set birth date
		if birthdate is None:
			update_command = update_command + ", Birthdate = null "
		else :
			update_command = update_command + ", Birthdate = '" + birthdate + "' "

		# upload image is user specified
 		if form.has_key('image_file'):
			
    			fileitem = form['image_file']
    			if fileitem.file :
				extension = os.path.splitext(fileitem.filename)[1] 
				if extension != '' :
					fout = file ("model/writers/illustrator-" +  name  + extension , 'wb')
    					while 1:
        					chunk = fileitem.file.read(100000)
        					if not chunk: break
        					fout.write(chunk)
    					fout.close()
					update_command = update_command + ", IllustratorImage = '" + "model/writers/illustrator-" +  name + extension  + "' "
		

		update_command = update_command + "WHERE IllustratorName = '" + name + "'"
		cur.execute(update_command)

		# Associate Books to Writer
		command = "DELETE FROM BookIllustrator WHERE IllustratorName = '" + name + "'"
		cur.execute(command)
                for book in illustratorbooks:
                	command = "INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES (" + book + ",'"  + name + "')"
                        cur.execute(command)
			
		con.commit() 
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user_= cur.fetchone() #

		command = "SELECT * from Illustrators WHERE IllustratorName ='" + name + "'"
		cur.execute(command)
		illustrator_ = cur.fetchone()

		command = "SELECT ISBN, Title, Price, Image from ComicBooks NATURAL JOIN BookIllustrator NATURAL JOIN Illustrators WHERE IllustratorName='" + name + "'"
		
		cur.execute(command)
		rows = cur.fetchall()
		titles = []
		for row in rows:
			titles.append(row)

		command = "SELECT Genre from ComicBooks NATURAL JOIN BookGenre NATURAL JOIN BookIllustrator WHERE IllustratorName ='" + name + "'"
		cur.execute(command)
		genres = cur.fetchall()
		genres_ = []
		for genre in genres:
			if genre not in genres_:
				genres_.append(genre)

                sidebar = utilities.getSideBar(email,user_[9], cur)
		successmsg = '<strong>Success:</strong> Illustrator has been saved.'
		print display("illustrator-profile.html").render(sidebar=sidebar,user=user_,illustrator=illustrator_,titles=titles,genres=genres_,success=successmsg)		
                sess.close()				
	
	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
