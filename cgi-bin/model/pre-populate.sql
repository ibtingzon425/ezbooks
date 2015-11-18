INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780930289232", "DC Comics Inc", "1986-09-01",  "Watchmen", "899.00", "416", "model/images/9780930289232.jpg", "This Hugo Award-winning graphic novel chronicles the fall from grace of a group of super-heroes plagued by all-too-human failings. Along the way, the concept of the super-hero is dissected as the heroes are stalked by an unknown assassin. <br><br> One of the most influential graphic novels of all time and a perennial best-seller, Watchmen has been studied on college campuses across the nation and is considered a gateway title, leading readers to other graphic novels such as V for Vendetta, Batman: The Dark Knight Returns and The Sandman series. ");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage, WriterDescription) VALUES ("Alan Moore", "Male", "Northampton, England, The United Kingdom", "model/writers/alan-moore.jpg", "Alan Moore is an English writer primarily known for his work in comic books including Watchmen, V for Vendetta, and From Hell.");
INSERT INTO BookWriter(ISBN, WriterId) VALUES ("9780930289232", LAST_INSERT_ID());

INSERT INTO Illustrators(IllustratorName, Gender, Born, IllustratorImage, IllustratorDescription) VALUES ("Dave Gibbons", "Male", "The United Kingdom", "model/writers/dave-gibbons.jpg", "Dave Gibbons is an English comic book artist, writer and sometime letterer. He is best known for his collaborations with writer Alan Moore, which include the miniseries Watchmen and the Superman story. ");
INSERT INTO BookIllustrator(ISBN, IllustratorId) VALUES ("9780930289232", LAST_INSERT_ID());

INSERT INTO BookFormat(ISBN, Format) VALUES ("9780930289232", ".cbr");
INSERT INTO BookFormat(ISBN, Format) VALUES ("9780930289232", ".cbz");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Crime Fiction");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Science Fiction");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Superhero");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Hugo Award (1988)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Locus Award for Best Non-Fiction/Art (1988)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Urhunden Prize for Foreign Album (1992) ");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781608866878 ", "BOOM! Box ", "2015-04-07",  "Lumberjanes, Vol. 1: Beware the Kitten Holy", "399.00", "128", "model/images/9781608866878.jpg", "Jo, April, Mal, Molly and Ripley are five best pals determined to have an awesome summer together...and they're not gonna let any insane quest or an array of supernatural critters get in their way! Not only is it the second title launching in our new BOOM! Box imprint but LUMBERJANES is one of those punk rock, love-everything-about-it stories that appeals to fans of basically all excellent things. ");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage, WriterDescription) VALUES ("Noelle Stevenson", "Female", "Los Angeles, California ", "model/writers/noelle-stevenson.jpg", "Noelle Stevenson is a comic artist and freelance illustrator residing in Los Angeles, California. ");
INSERT INTO BookWriter(ISBN, WriterId) VALUES ("9781608866878", LAST_INSERT_ID());
INSERT INTO Writers(WriterName, Gender) VALUES ("Grace Ellis", "Female");
INSERT INTO BookWriter(ISBN, WriterId) VALUES ("9781608866878", LAST_INSERT_ID());

INSERT INTO Illustrators(IllustratorName, Gender, IllustratorImage) VALUES ("Brooke A. Allen", "Female", "model/writers/brooke-allen.jpg");
INSERT INTO BookIllustrator(ISBN, IllustratorId) VALUES ("9781608866878", LAST_INSERT_ID());

INSERT INTO BookFormat(ISBN, Format) VALUES ("9781608866878", ".cbr");
INSERT INTO BookFormat(ISBN, Format) VALUES ("9781608866878", ".cbz");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Slice of Life");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781608866878", "Will Eisner Comic Industry Awards for Best New Series & Best Publication for Teens (ages 13-17) (2015)")
