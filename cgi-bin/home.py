#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt

#Redirects user to home.html

def main():
	form = cgi.FieldStorage()
	username = form.getvalue('username')
	
	print display("home.html").render(username=username)

if __name__ == '__main__':
	main()