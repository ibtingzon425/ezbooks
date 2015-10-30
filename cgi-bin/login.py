#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from template import display
import time, os, datetime, Cookie

def invalidLogin():
	print "<script type='text/javascript'> \
	          alert('Incorrect email or password.');\
	          </script>" 

def cookieValidationFailed():
	print "<script type='text/javascript'> \
	          alert('Session Expired. Please log in.');\
	          </script>" 

def main():
	form = cgi.FieldStorage()
	code = form.getvalue('redirect')

	print display("login.html").render(user=None)
	if(code == '0'):
		invalidLogin()
	elif(code == '1'):
		cookieValidationFailed()

if __name__ == '__main__':
    main()
