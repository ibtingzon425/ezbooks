#!/usr/bin/python
import cgi, jinja2
import cgitb; cgitb.enable()
from jinja2 import Environment, PackageLoader, FileSystemLoader

env = Environment(loader=FileSystemLoader('./view'))

def readTemplateFile(templateFile):
	template = env.get_template(templateFile)
	return template

def display(temp):  
	display = readTemplateFile(temp)
	print "Content-Type: text/html"
	print ""
	return display
