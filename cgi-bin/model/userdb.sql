DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Books;

CREATE TABLE Users(
	fname VARCHAR(100) NOT NULL,
	lname  VARCHAR(100) NOT NULL,
	email VARCHAR(50) PRIMARY KEY,
	password VARCHAR(256) NOT NULL);

CREATE TABLE Books(
	ISBN INT PRIMARY KEY,
	title VARCHAR(256) NOT NULL,
	author VARCHAR(256) NOT NULL,
	price DECIMAL(10,2) NOT NULL, 
	publisher VARCHAR(256), 
	description VARCHAR(500),
	format VARCHAR(100),
	genre VARCHAR(100));

INSERT INTO Users(fname, lname, password, email) VALUES('Timmy', 'Chu', '12346', 'timmychu@gmail.com');
INSERT INTO Users(fname, lname, password, email) VALUES('Honorede', 'Balzac', '12345', 'balzac@yahoo.com.ph');
INSERT INTO Books(ISBN, price, title, author, publisher, description) VALUES("45679101", "100.99", "1984", "George Orwell", "Mgraw Hills", "Dystopian")
