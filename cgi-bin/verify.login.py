#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt

#Verifies that login credentials (username, password) are correct

def invalidLogin():
	print display("login.html").render()
	print "<script type='text/javascript'> \
	          alert('Incorrect username or password.');\
	          </script>" 

def validateLoginCredentials(username, password):
	cur = con.cursor()

	command = "SELECT password FROM Users WHERE username = %s";
	cur.execute(command, (username))
	row = cur.fetchone()
	if (row != None):
		enc_password = row[0]
		verify = sha512_crypt.verify(password, enc_password)
		if (verify):
			print "Location: home.py?username=" + username + "\r\n"
		else:
			invalidLogin() 
	else:
		invalidLogin()

def main():
	form = cgi.FieldStorage()
	username = form.getvalue('username')
	password = form.getvalue('password')

	validateLoginCredentials(username, password)

if __name__ == '__main__':
	main()
