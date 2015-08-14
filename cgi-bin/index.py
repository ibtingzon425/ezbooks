#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb as mdb
from template_manager import display

def display_data(name, age):
    print "<HTML>\n"
    print "<HEAD>\n"
    print "\t<TITLE>Info Form</TITLE>\n"
    print "</HEAD>\n"
    print "<BODY BGCOLOR = white>\n"
    print name, ", you are", age, "years old."
    print "</BODY>\n"
    print "</HTML>\n"

def main():
    form = cgi.FieldStorage()
    if (form.has_key("action") and form.has_key("name") \
    and form.has_key("age")):
             if (form["action"].value == "display"):
                display_data(form["name"].value, form["age"].value)
    else:
            display()

if __name__ == '__main__':
    main()
