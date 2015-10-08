INSERT INTO Users(FirstName, LastName, Password, Email) VALUES('Timmy', 'Chu', '12346', 'timmychu@gmail.com');
INSERT INTO Users(FirstName, LastName, Password, Email) VALUES('Honorede', 'Balzac', '12345', 'balzac@yahoo.com.ph');

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Malala", "Yousafzai");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("9780297870920", "I Am Malala", "599.49", LAST_INSERT_ID(), "model/images/IAmMalala.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("9780297870920", "Non-Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("George", "Orwell");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("1234555670321", "1984", "599.99", LAST_INSERT_ID(), "model/images/1984.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("1234555670321", "Science Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Anthony", "Doerr");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("1540555475320", "All the Light We Cannot See", "499.49", LAST_INSERT_ID(), "model/images/AllTheLightWeCannotSee.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("1540555475320", "General Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("JD", "Salinger");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("9580555470320", "Catcher in the Rye", "399.49", LAST_INSERT_ID(), "model/images/CatcherInTheRye.png");
INSERT INTO Genres(ISBN, Genre) VALUES ("9580555470320", "General Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Aldous", "Huxley");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("2345565470322", "Brave New World", "799.49", LAST_INSERT_ID(), "model/images/BraveNewWorld.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("2345565470322", "Science Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Harper", "Lee");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("5587555470326", "To Kill a Mockingbird", "499.99", LAST_INSERT_ID(), "model/images/ToKillAMockingbird.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("5587555470326", "General Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("Barbara", "Demick");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("7787755470326", "Nothing to Envy", "799.99", LAST_INSERT_ID(), "model/images/NothingToEnvy.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("7787755470326", "Non-Fiction");

INSERT INTO Authors (AuthorFirstName, AuthorLastName) VALUES ("George", "Martin");
INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("1787755456789", "A Clash of Kings", "599.99", LAST_INSERT_ID(), "model/images/AClashOfKings.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("1787755456789", "Fantasy");

INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("8347755456789", "A Dance With Dragons", "599.99", LAST_INSERT_ID(), "model/images/ADanceWithDragons.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("8347755456789", "Fantasy");

INSERT INTO Books(ISBN, Title, Price, AuthorId, Image) VALUES ("3347755456789", "A Storm of Swords", "599.99", LAST_INSERT_ID(), "model/images/AStormOfSwords.jpg");
INSERT INTO Genres(ISBN, Genre) VALUES ("3347755456789", "Fantasy")