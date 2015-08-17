DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	username VARCHAR(25) PRIMARY KEY, 
	password VARCHAR(256) NOT NULL, 
	email VARCHAR(100));
INSERT INTO Users(username, password, email) VALUES('TimmyChu', '12346', 'timmychu@gmail.com');
INSERT INTO Users(username, password, email) VALUES('HonoredeBalzac', '12345', 'balzac@yahoo.com.ph')
