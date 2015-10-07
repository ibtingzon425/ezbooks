#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con
from passlib.hash import sha512_crypt
import os, time, sys, session, Cookie


def main():
	form = cgi.FieldStorage()
	
	name = form.getvalue('name')
	sess = session.Session(expires=365*24*60*60, cookie_path='/')

	try:
		print display("home.html").render(name=name)
	except Exception:
		sess.cookieValidationFailed("Here")

if __name__ == '__main__':
	main()