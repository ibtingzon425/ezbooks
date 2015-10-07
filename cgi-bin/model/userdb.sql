DROP TABLE IF EXISTS Shelf;
DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
	FirstName VARCHAR(100) NOT NULL,
	LastName  VARCHAR(100) NOT NULL,
	Email VARCHAR(50) PRIMARY KEY,
	Password VARCHAR(256) NOT NULL
);

CREATE TABLE Books(
	ISBN INT PRIMARY KEY,
	Title VARCHAR(256) NOT NULL,
	Price DECIMAL(10,2) NOT NULL,
	AuthorId INT NOT NULL, 
	Publisher VARCHAR(256), 
	Description VARCHAR(500),
	Image VARCHAR(50)
);

CREATE TABLE Authors(
	AuthorId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	AuthorFirstName VARCHAR(256) NOT NULL,
	AuthorLastName VARCHAR(256) NOT NULL
);

CREATE TABLE Genres(
	ISBN INT NOT NULL,
	Genre VARCHAR(50) NOT NULL,
	PRIMARY KEY(ISBN, Genre)
); 

CREATE TABLE Reviews(
	ISBN INT NOT NULL, 
	Review VARCHAR(500) NOT NULL,
	Email VARCHAR(50) NOT NULL,
	PRIMARY KEY(ISBN, Review)
);

CREATE TABLE Shelf(
	Email VARCHAR(50) NOT NULL,
	ISBN INT NOT NULL,
	PRIMARY KEY(Email, ISBN) 
);

ALTER TABLE Books ADD FOREIGN KEY (AuthorId) REFERENCES Authors(AuthorId);
ALTER TABLE Genres ADD FOREIGN KEY (ISBN) REFERENCES Books(ISBN);
ALTER TABLE Reviews ADD FOREIGN KEY (ISBN) REFERENCES Books(ISBN);
ALTER TABLE Reviews ADD FOREIGN KEY (Email) REFERENCES Users(Email);
ALTER TABLE Shelf ADD FOREIGN KEY(Email) References Users(Email);
ALTER TABLE Shelf ADD FOREIGN KEY(ISBN) References Books(ISBN);

INSERT INTO Users(FirstName, LastName, Password, Email) VALUES('Timmy', 'Chu', '12346', 'timmychu@gmail.com');
INSERT INTO Users(FirstName, LastName, Password, Email) VALUES('Honorede', 'Balzac', '12345', 'balzac@yahoo.com.ph');

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("George", "Orwell");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("1234567", "1984", "350.49", LAST_INSERT_ID(), "model/images/1984.jpg");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Harper", "Lee");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("34567890", "To Kill a Mockingbird", "500.00", LAST_INSERT_ID(), "model/images/ToKillAMockingbird.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("34567890", "Bildungsroman");
INSERT INTO Genres(ISBN, Genre) VALUES ("34567890", "Fiction")
