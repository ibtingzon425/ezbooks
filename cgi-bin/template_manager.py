#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

TemplateFile = ("./html/template.html")

def display(): 
    TemplateHandle = open(TemplateFile, "r")
    TemplateInput = TemplateHandle.read()     
    TemplateHandle.close()                

    print "Content-Type: text/html"
    print ""
    print TemplateInput 
