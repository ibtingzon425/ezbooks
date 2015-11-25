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
	
	userprofile = form.getvalue('user') #email of userprofile
	email = form.getvalue('email') #email of current user
        action = form.getvalue('action') # action 

	#TODO: If current user != email 

	try:
		cur = con.cursor()
		
		command = "SELECT * FROM Users WHERE Email = '" + email + "'";
		cur.execute(command)
		user= cur.fetchone() #

		if action != 'create' :
			command = "SELECT * FROM Users WHERE Email = '" + userprofile + "'";
			cur.execute(command)
			userprof = cur.fetchone() #

			command = "SELECT * from ComicBooks NATURAL JOIN UserCart WHERE Email='" + userprofile + "'"
		
			cur.execute(command)
			rows = cur.fetchall()
			titles = []
			for row in rows:
				titles.append(row)

			command = "SELECT * from ComicBooks NATURAL JOIN UserOwned WHERE Email='" + userprofile + "'"
		
			cur.execute(command)
			rows = cur.fetchall()
			own = []
			for row in rows:
				own.append(row)

		sidebar = utilities.getSideBar(email,user[9], cur)
		
		if action == 'edit':
			countryDropDown = utilities.generateCountryDropDown(userprof[5]) 
			print display("user-profile-edit.html").render(user=user,userprof=userprof,sidebar=sidebar,titles=titles,own=own,countryDropDown=countryDropDown)
		elif action == 'create':
			countryDropDown = utilities.generateCountryDropDown(None)
			print display("user-profile-create.html").render(user=user,createform=None,sidebar=sidebar,countryDropDown=countryDropDown)	
		else :
			print display("user-profile.html").render(user=user,userprof=userprof,sidebar=sidebar,titles=titles,own=own)

	except mdb.Error, e:
	    if con:
	        con.rollback()

if __name__ == '__main__':
	main()
