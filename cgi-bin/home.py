#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie

def cookieValidationFailed():
	print display("login.html").render()
	print "<script type='text/javascript'> \
	          alert('Session Expired. Please log in.');\
	          </script>" 

def invaidPageError():
	print display("login.html").render()
	print "<script type='text/javascript'> \
	          alert('Error occurred. Please try again.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	
	fname = form.getvalue('fname')
	lname = form.getvalue('lname')
	sess = session.Session(expires=365*24*60*60, cookie_path='/')

	try:
		if(lname and fname):
			print display("home.html").render(fname=fname,lname=lname)
		else:
			invaidPageError()
	except Exception:
		cookieValidationFailed()

if __name__ == '__main__':
	main()