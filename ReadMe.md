# CS 270 Final Project
## Requirements
* Linux OS: Ubuntu 14.0
* apache2 
* Python 2.7.6
* mysql Ver 14.14 

To install and connect MYSQL to Python,

	sudo apt-get install mysql-server
	sudo apt-get install python-mysqldb

## Configuring Python CGI to Apache  

1. Enable cgi using the command: sudo a2enmod cgi
	
	optional: install python support: 
		sudo apt-get install libapache2-mod-python

2. Add the following lines to /etc/apache2/apache2.conf
	
	```
	ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
	<Directory "/var/www/cgi-bin">
	   AllowOverride None
	   Options ExecCGI
	   AddHandler cgi-script .cgi .py
	   Order allow,deny
	   Allow from all
	</Directory>

	<Directory "/var/www/cgi-bin">
	Options All
	</Directory>
	```

3. In  /var/www/ create folder 'cgi-bin'. This is where all cgi files will be stored. 
Go to http://localhost/cgi-bin/<cgi_file.py>

## Checking apache if running:

	sudo service apache2 status
	sudo service apache2 start
	sudo service apache2 restart

## To access MySQL: 

	mysql -u root -p password
