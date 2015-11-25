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
	
	userprof_form = form.getvalue('user') #email of userprofile
	email = form.getvalue('email') #email of current user
	firstname = form.getvalue('first_name')
	lastname = form.getvalue('last_name')
	password = form.getvalue('password')
	country = form.getvalue('country')
	birthdate = form.getvalue('birth_date')
	is_administrator = form.getvalue('is_administrator') 	

	#TODO: If current user != email 

	try:
		cur = con.cursor()

		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
                cur.execute(command)
                user= cur.fetchone()

		command = "SELECT * FROM Users WHERE Email = '" + userprof_form + "'";
                cur.execute(command)
                userprof= cur.fetchone()		
		

		sidebar = utilities.getSideBar(email,user[9], cur)
		
		if userprof is not None :
			createform = []
			createform.append(userprof_form)
			createform.append(firstname)
			createform.append(lastname)
			createform.append(password)
			createform.append(birthdate)
			createform.append(is_administrator)

			error = 'User with email ' + userprof_form + ' already exists.' 
                        countryDropDown = utilities.generateCountryDropDown(country)	
			print display("user-profile-create.html").render(user=user,createform=createform,sidebar=sidebar,countryDropDown=countryDropDown,error=error)
		else :
			# Required Fields
			enc_password = sha512_crypt.encrypt(password)
			insert_command_1 = "INSERT INTO Users(FirstName, LastName, Email, Password, IsAdmin, Datejoined "
			insert_command_2 = "VALUES ( '" + firstname + "','" + lastname + "','" + userprof_form + "','" + enc_password  + "','" + is_administrator +  "', NOW() "

			# Country
			if country is not None:
				insert_command_1 = insert_command_1 + ", Country "
				insert_command_2 = insert_command_2 + " ,'" + country + "' "

			# Birthdate
			if birthdate is not None:
				insert_command_1 = insert_command_1 + ", Birthdate "
				insert_command_2 = insert_command_2 + " ,'" + birthdate + "' "
						
			 # upload image is user specified
                	if form.has_key('image_file'):

                        	fileitem = form['image_file']
                        	if fileitem.file :
                                	extension = os.path.splitext(fileitem.filename)[1]
                                	if extension != '' :
                                        	fout = file ("model/users/" +  email + extension , 'wb')
                                        	while 1:
                                                	chunk = fileitem.file.read(100000)
                                                	if not chunk: break
                                                	fout.write(chunk)
                                        	fout.close()
                                        	insert_command_1 = insert_command_1 + ", Image " 
						insert_command_2 = insert_command_2 + ", 'model/users/" +  email + extension  + "' "


			insert_command_1 = insert_command_1 + ") "
			insert_command_2 = insert_command_2 + ") " 
			cur.execute(insert_command_1 + insert_command_2)
                	con.commit()

		

			command = "SELECT * FROM Users WHERE Email = '" + userprof_form + "'";
                	cur.execute(command)
                	userprof = cur.fetchone() #

                	command = "SELECT * from ComicBooks NATURAL JOIN UserCart WHERE Email='" + email + "'"

                	cur.execute(command)
                	rows = cur.fetchall()
                	titles = []
                	for row in rows:
                        	titles.append(row)

                	command = "SELECT * from ComicBooks NATURAL JOIN UserOwned WHERE Email='" + email + "'"

                	cur.execute(command)
                	rows = cur.fetchall()
                	own = []
                	for row in rows:
                        	own.append(row)

                	sidebar = utilities.getSideBar(email,user[9], cur)
                	print display("user-profile.html").render(user=user,userprof=userprof,sidebar=sidebar,titles=titles,own=own)			

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
