#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import sha, time, os, datetime, session

#Verifies that login credentials (username, password) are correct
#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import sha, time, os, datetime, session
import os, time, sys, session, Cookie, json
import utilities

#Verifies that login credentials (username, password) are correct

def main():
	try:
		form = cgi.FieldStorage()
		email= form.getvalue('email')
		password = form.getvalue('password')
		
		cur = con.cursor()
		command = "SELECT password FROM Users WHERE email = %s";
		cur.execute(command, (email))
		row = cur.fetchone()
		
		if (row != None):
			enc_password = row[0]
			verify = sha512_crypt.verify(password, enc_password)
			if (verify):
				sess = session.Session(expires=365*24*60*60, cookie_path='/')
				sess.data['lastvisit'] = repr(time.time())
				sess.data['user'] = email
				print "Location: home.py?\r\n"
			else:
				print "Location: login.py?redirect=0\r\n"
		else:
			print "Location: login.py?redirect=0\r\n"
	except KeyError:
		print "Location: login.py\r\n"

if __name__ == '__main__':
	main()
