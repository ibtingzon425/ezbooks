#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
import Cookie

def main():
    form = cgi.FieldStorage()

    username = form.getvalue('username')
    password = form.getvalue('password')

    print display("home.html").render(username=username)

    

if __name__ == '__main__':
    main()