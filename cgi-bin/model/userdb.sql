SET FOREIGN_KEY_CHECKS=0; 
DROP TABLE IF EXISTS BookGenre;
DROP TABLE IF EXISTS Genres;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Writers;
DROP TABLE IF EXISTS Illustrators;
DROP TABLE IF EXISTS BookWriter;
DROP TABLE IF EXISTS BookIllustrator;
DROP TABLE IF EXISTS ComicBooks;
DROP TABLE IF EXISTS UserCart;
DROP TABLE IF EXISTS UserOwned;
DROP TABLE IF EXISTS LiteraryAwards;

CREATE TABLE Users(
	FirstName VARCHAR(100) NOT NULL,
	LastName  VARCHAR(100) NOT NULL,
	Email VARCHAR(50) PRIMARY KEY,
	Password VARCHAR(256) NOT NULL,
	DateJoined DATE, 
	Country VARCHAR(50) DEFAULT "",
	Birthdate DATE,
	Image VARCHAR(500) DEFAULT "model/users/default.png",
	TotalCost DECIMAL(10,2),
    IsAdmin CHAR(1) DEFAULT 'N'
);

CREATE TABLE ComicBooks(
	ISBN VARCHAR(500) PRIMARY KEY,
	Title VARCHAR(256) NOT NULL,
	Price DECIMAL(10,2) NOT NULL,
	Publisher VARCHAR(256) DEFAULT "", 
	Description VARCHAR(5000) DEFAULT "No description available.",
	Image VARCHAR(500) DEFAULT "model/writers/default.png",
	DatePublished DATE,
	Length INTEGER DEFAULT 0,
	Format VARCHAR(500) DEFAULT "Information not available."
);

CREATE TABLE Writers(
	WriterName VARCHAR(256) PRIMARY KEY,
	WriterDescription VARCHAR(5000) DEFAULT "No description available.",
	Birthdate DATE,
	Born VARCHAR(50) DEFAULT "",
	Gender VARCHAR(10) DEFAULT "",
	WriterImage VARCHAR(50) DEFAULT "model/writers/default.png"
);

CREATE TABLE Illustrators(
	IllustratorName VARCHAR(256) PRIMARY KEY,
	IllustratorDescription VARCHAR(5000) DEFAULT "No description available.",
	Birthdate DATE,
	Born VARCHAR(50) DEFAULT "",
	Gender VARCHAR(10) DEFAULT "",
	IllustratorImage VARCHAR(50) DEFAULT "model/writers/default.png"
);

CREATE TABLE Genres(
	Genre VARCHAR(50) PRIMARY KEY,
	GenreDesc VARCHAR(500)
); 

CREATE TABLE BookWriter(
	ISBN VARCHAR(500) NOT NULL,
	WriterName VARCHAR(256) NOT NULL,
	PRIMARY KEY(ISBN, WriterName)
);

CREATE TABLE BookIllustrator(
	ISBN VARCHAR(500) NOT NULL,
	IllustratorName VARCHAR(256) NOT NULL,
	PRIMARY KEY(ISBN, IllustratorName)
);

CREATE TABLE BookGenre(
	ISBN VARCHAR(500) NOT NULL,
	Genre VARCHAR(50) NOT NULL,
	PRIMARY KEY(ISBN, Genre)
); 

CREATE TABLE LiteraryAwards(
	ISBN VARCHAR(500) NOT NULL,
	Award VARCHAR(500),
	PRIMARY KEY(ISBN, Award) 
);

CREATE TABLE UserCart(
	Email VARCHAR(50) NOT NULL,
	ISBN VARCHAR(500) NOT NULL,
	PRIMARY KEY(Email, ISBN) 
);

CREATE TABLE UserOwned(
	Email VARCHAR(50) NOT NULL,
	ISBN VARCHAR(500) NOT NULL,
	PRIMARY KEY(Email, ISBN) 
);

ALTER TABLE BookGenre ADD FOREIGN KEY (ISBN) REFERENCES ComicBooks(ISBN);
ALTER TABLE BookGenre ADD FOREIGN KEY (Genre) REFERENCES Genres(Genre);
ALTER TABLE BookReview ADD FOREIGN KEY (ISBN) REFERENCES ComicBooks(ISBN);
ALTER TABLE BookReview ADD FOREIGN KEY (Email) REFERENCES Users(Email);
ALTER TABLE UserCart ADD FOREIGN KEY(Email) References Users(Email);
ALTER TABLE UserCart ADD FOREIGN KEY(ISBN) References ComicBooks(ISBN);
ALTER TABLE BookWriter ADD FOREIGN KEY(ISBN) References ComicBooks(ISBN);
ALTER TABLE BookWriter ADD FOREIGN KEY(WriterName) References Writers(WriterName);
ALTER TABLE BookIllustrator ADD FOREIGN KEY(ISBN) References ComicBooks(ISBN);
ALTER TABLE BookIllustrator ADD FOREIGN KEY(IllustratorName) References Illustrators(IllustratorName)   
