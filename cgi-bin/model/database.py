#Creates and populates table
# Create testuser and grant access using the following commands:
	# SHOW DATABASES;
	# CREATE DATABASE testdb;
	# CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
	# USE testdb;
	# GRANT ALL ON testdb.* TO 'testuser'@'localhost';

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

#In .sql file, all commands should be separated with a semicolon (;)
def execute_sql(filename):
	try:
		fd = open(filename, 'r')
		sqlFile = fd.read()
		fd.close()

		sqlCommands = sqlFile.split(';')

		with con:
			cur = con.cursor()
			for command in sqlCommands:
				cur.execute(command)

	except mdb.Error, e:
	    if con:
	        con.rollback()
	    
	    print "Error %d: %s" % (e.args[0],e.args[1])
	    sys.exit(1)

def main():
    execute_sql('userdb.sql')
    execute_sql('pre-populate.sql')

    if con:
    	con.close()

if __name__ == '__main__':
    main()