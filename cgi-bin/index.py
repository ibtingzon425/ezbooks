#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display, dict

def main():
    form = cgi.FieldStorage()
    display(dict['login'])
    username =  form.getvalue('username')
    if "Submit1" in form:
        print username 

if __name__ == '__main__':
    main()
