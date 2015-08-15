#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template import display
from model.database import con

def main():
    form = cgi.FieldStorage()

    username = form.getvalue('username')
    password = form.getvalue('password')
    email = form.getvalue('email')

    print display("home.html").render(username=username)

    command = "INSERT INTO Users(username, password, email) VALUES(%s, %s, %s)"

    try:
        cur = con.cursor()
        cur.execute(command, (username, password, email))
        con.commit()

    except mdb.Error, e:
        if con:
            con.rollback()

if __name__ == '__main__':
    main()