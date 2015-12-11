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
	
	#userprof_form = form.getvalue('user') #email of userprofile
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

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
                cur.execute(command)
                user= cur.fetchone()

		command = "SELECT * from Illustrators WHERE lower(IllustratorName)=lower('" + name + "')"
		cur.execute(command)
		writer_ = cur.fetchone()		
		

		sidebar = utilities.getSideBar(email,user[9], cur)
		
		if writer_  is not None :
			createform = []
			createform.append(name)
			createform.append(birthdate)
			createform.append(gender)
			createform.append(description)

			error = '<strong>Database Error:</strong> Illustrator with name ' + name + ' already exists.' 
                        countryDropDown = utilities.generateCountryDropDown(born)
			bookitems = utilities.getBookItems(illustratorbooks, cur)	
			print display("illustrator-profile-create.html").render(user=user,createform=createform,sidebar=sidebar,countryDropDown=countryDropDown,error=error,bookitems=bookitems)
		else :
			# Required Fields
			insert_command_1 = "INSERT INTO Illustrators(IllustratorName "
			insert_command_2 = "VALUES ( '" + name + "'"

			# Born / Country
			if born is not None:
				insert_command_1 = insert_command_1 + ", Born "
				insert_command_2 = insert_command_2 + " ,'" + born + "' "

			# Birthdate
			if birthdate is not None:
				insert_command_1 = insert_command_1 + ", Birthdate "
				insert_command_2 = insert_command_2 + " ,'" + birthdate + "' "

			# Gender
			if gender is not None :
				insert_command_1 = insert_command_1 + ", Gender "
				insert_command_2 = insert_command_2 + " ,'" + gender + "' "

			# Description
			if description is not None:
				insert_command_1 = insert_command_1 + ", IllustratorDescription "
                                insert_command_2 = insert_command_2 + " ,'" + description + "' "
		
			 # upload image is user specified
                	if form.has_key('image_file'):

                        	fileitem = form['image_file']
                        	if fileitem.file :
                                	extension = os.path.splitext(fileitem.filename)[1]
                                	if extension != '' :
                                        	fout = file ("model/writers/illustrator-" +  name + extension , 'wb')
                                        	while 1:
                                                	chunk = fileitem.file.read(100000)
                                                	if not chunk: break
                                                	fout.write(chunk)
                                        	fout.close()
                                        	insert_command_1 = insert_command_1 + ", IllustratorImage " 
						insert_command_2 = insert_command_2 + ", 'model/writers/illustrator-" +  name + extension  + "' "


			insert_command_1 = insert_command_1 + ") "
			insert_command_2 = insert_command_2 + ") " 
			cur.execute(insert_command_1 + insert_command_2)

			# Associate Books to Writer
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

                	sidebar = utilities.getSideBar(email,user[9], cur)
			successmsg = '<strong>Success:</strong> Illustrator has been created.'
			print display("illustrator-profile.html").render(sidebar=sidebar,user=user_,illustrator=illustrator_,titles=titles,genres=genres_,success=successmsg)		
                	sess.close()
	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
