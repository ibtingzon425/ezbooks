#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from template import display
import urllib, urllib2
import os, time, Cookie

# Renders/displays Registration page
def passwordError():
	print "<script type='text/javascript'> \
            alert('Confirmed password did not match. Please try again.');\
            </script>"

def emailExistsError():
	print "<script type='text/javascript'> \
            alert('An account already exists for this email address.');\
            </script>"

def main():
    form = cgi.FieldStorage()
    code = form.getvalue('redirect')

    print display("reg.html").render(user=None)
    if(code == '0'):
    	emailExistsError()
    elif(code == '1'):
    	passwordError()

if __name__ == '__main__':
    main()
