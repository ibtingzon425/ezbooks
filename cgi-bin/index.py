#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
from template import display
import urllib, urllib2

# Renders/displays Registration page

def main():
    form = cgi.FieldStorage()
    print display("reg.html").render()

if __name__ == '__main__':
    main()