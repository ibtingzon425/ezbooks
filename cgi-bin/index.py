#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from template import display
import urllib, urllib2
import os, time, Cookie

# Renders/displays Registration page

def invalidReg():
	print "<script type='text/javascript'> \
            alert('An account already exists for this email address.');\
            </script>"

def main():
    form = cgi.FieldStorage()
    code = form.getvalue('redirect')

    print display("reg.html").render()
    if(code == '0'):
    	invalidReg()

if __name__ == '__main__':
    main()
