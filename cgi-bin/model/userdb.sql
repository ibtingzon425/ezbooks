DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	fname VARCHAR(50) NOT NULL,
	lname  VARCHAR(50) NOT NULL,
	email VARCHAR(100) PRIMARY KEY,
	password VARCHAR(256) NOT NULL);
INSERT INTO Users(fname, lname, password, email) VALUES('Timmy', 'Chu', '12346', 'timmychu@gmail.com');
INSERT INTO Users(fname, lname, password, email) VALUES('Honorede', 'Balzac', '12345', 'balzac@yahoo.com.ph')
