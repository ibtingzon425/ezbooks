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
	email = form.getvalue('email') #email of current user
	firstname = form.getvalue('first_name')
	lastname = form.getvalue('last_name')
	current_password = form.getvalue('current_password')
	new_password = form.getvalue('new_password')
	country = form.getvalue('country')
	birthdate = form.getvalue('birth_date')	

	#TODO: If current user != email 

	try:

		cur = con.cursor()

		update_command = "UPDATE Users SET FirstName = '" + firstname + "', LastName = '" + lastname + "' "

		# check if password changed
		if current_password != new_password :
			enc_password = sha512_crypt.encrypt(new_password)
			update_command = update_command + ", Password = '" + enc_password + "' "

		# set country
		if country is None:
			update_command = update_command + ", Country = null "
		else :
			update_command = update_command + ", Country = '" + country + "' " 

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
					fout = file ("model/users/" +  email + extension , 'wb')
    					while 1:
        					chunk = fileitem.file.read(100000)
        					if not chunk: break
        					fout.write(chunk)
    					fout.close()
					update_command = update_command + ", Image = '" + "model/users/" +  email + extension  + "' "
		

		update_command = update_command + "WHERE Email = '" + userprof + "'"
		cur.execute(update_command)
		con.commit() 
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() #

		command = "SELECT * FROM Users WHERE Email = '" + userprof + "'";
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
