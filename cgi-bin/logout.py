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
		
		sess = session.Session(expires=0, cookie_path='/')
		sess.data['user'] = None
		print "Location: login.py?\r\n"

	except KeyError:
		print "Location: login.py\r\n"

if __name__ == '__main__':
	main()
