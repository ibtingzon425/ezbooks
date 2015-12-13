-- Real Password is 12345
INSERT INTO `Users` VALUES ('Admin','User','admin@ezcomics.com','$6$rounds=656000$wVf.fA291z66gi1k$6DuEkfdkorc1LRKQOJLMHcKJhhxK0W3k5FVhIO1mfxQwvky.ucTbQNPgHrGJd2d71suI8qCYWPXMbk2L/.q4k/','2015-11-25',NULL,NULL,'model/users/default.png',NULL,'Y');

-- Real Password is 0987
INSERT INTO `Users` VALUES 
('Roy Amante','Salvador','roy.salvador@gmail.com','$6$rounds=656000$4SjJk0DANLFXwHG.$bUYDV4GAmkpXudefgrZ7Puw8UnWJgrTgHY4XBnLt0QfKtzIcC6O/spq3x7Q8NNEsdIMeZjfkMoKnZFMPtWR7r1','2015-11-22',NULL,NULL,'model/users/default.png',0,'N');

INSERT INTO Genres (Genre, GenreDesc) VALUES ("Fantasy", "Fantasy is a genre that uses magic and other supernatural forms as a primary element of plot, theme, and/or setting.  ");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Humor", "A comic novel is usually a work of fiction in which the writer seeks to amuse the reader, sometimes with subtlety and as part of a carefully woven narrative, sometimes above all other considerations. ");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Crime Fiction", "The crime genre includes the broad selection of books on criminals, courts, and investigations.");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Science Fiction", "Science fiction (abbreviated SF or sci-fi with varying punctuation and capitalization) is a broad genre of fiction that often involves speculations based on current or future science or technology. ");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Action/Adventure", "Adventure fiction is a genre of fiction in which an adventure, an exciting undertaking involving risk and physical danger, forms the main storyline.");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Slice of Life", "Slice of life describes the use of realism depicting everyday experiences in art and entertainment");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Young Adult", "Young adult is a literary genre that focuses on characters and conflicts for readers aged between 12 and 18.");
INSERT INTO Genres (Genre, GenreDesc) VALUES ("Superhero", "Superhero is a type of speculative fiction examining the adventures of costumed crime fighters known as superheroes, who often possess superhuman powers and battle similarly powered criminals known as supervillains.");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780930289232", "DC", "1986-09-01",  "Watchmen", "899.00", "416", "model/images/9780930289232.jpg", "This Hugo Award-winning graphic novel chronicles the fall from grace of a group of super-heroes plagued by all-too-human failings. Along the way, the concept of the super-hero is dissected as the heroes are stalked by an unknown assassin. <br><br> One of the most influential graphic novels of all time and a perennial best-seller, Watchmen has been studied on college campuses across the nation and is considered a gateway title, leading readers to other graphic novels such as V for Vendetta, Batman: The Dark Knight Returns and The Sandman series. ");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage, WriterDescription) VALUES ("Alan Moore", "Male", "United Kingdom", "model/writers/alan-moore.jpg", "Alan Moore is an English writer primarily known for his work in comic books including Watchmen, V for Vendetta, and From Hell.");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780930289232", "Alan Moore");

INSERT INTO Illustrators(IllustratorName, Gender, Born, IllustratorImage, IllustratorDescription) VALUES ("Dave Gibbons", "Male", "United Kingdom", "model/writers/dave-gibbons.jpg", "Dave Gibbons is an English comic book artist, writer and sometime letterer. He is best known for his collaborations with writer Alan Moore, which include the miniseries Watchmen and the Superman story. ");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9780930289232", "Dave Gibbons");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Crime Fiction");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Science Fiction");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780930289232", "Superhero");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Hugo Award (1988)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Locus Award for Best Non-Fiction/Art (1988)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780930289232", "Urhunden Prize for Foreign Album (1992) ");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781608866878", "BOOM! Box", "2015-04-07",  "Lumberjanes, Vol. 1: Beware the Kitten Holy", "399.00", "128", "model/images/9781608866878.jpg", "Jo, April, Mal, Molly and Ripley are five best pals determined to have an awesome summer together...and they're not gonna let any insane quest or an array of supernatural critters get in their way! Not only is it the second title launching in our new BOOM! Box imprint but LUMBERJANES is one of those punk rock, love-everything-about-it stories that appeals to fans of basically all excellent things. ");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781608867370", "BOOM! Box", "2015-04-07",  "Lumberjanes, Vol. 2: Friendship to the Max", "399.00", "111", "model/images/9781608867370.jpg", "Jo, April, Mal, Molly, and Ripley are not your average campers and Miss Qiunzella Thiskwin Penniquiqul Thistle Crumpet's Camp for Hardcore Lady-Types is not your average summer camp. Between the river monsters, magic, and the art of friendship bracelets, this summer is only just beginning. Join the Lumberjanes as they take on raptors and a sibling rivalry that only myths are made of.");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780062278241", "BOOM! Box", "2015-08-12",  "Nimona", "399.00", "172", "model/images/9780062278241.jpg", "Nemeses! Dragons! Science! Symbolism! All these and more await in this brilliantly subversive, sharply irreverent epic from Noelle Stevenson. Featuring an exclusive epilogue not seen in the web comic, along with bonus conceptual sketches and revised pages throughout, this gorgeous full-color graphic novel is perfect for the legions of fans of the web comic and is sure to win Noelle many new ones.<br><br>Nimona is an impulsive young shapeshifter with a knack for villainy. Lord Ballister Blackheart is a villain with a vendetta. As sidekick and supervillain, Nimona and Lord Blackheart are about to wreak some serious havoc. Their mission: prove to the kingdom that Sir Ambrosius Goldenloin and his buddies at the Institution of Law Enforcement and Heroics aren't the heroes everyone thinks they are.");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage, WriterDescription) VALUES ("Noelle Stevenson", "Female", "United States", "model/writers/noelle-stevenson.jpg", "Noelle Stevenson is a comic artist and freelance illustrator residing in Los Angeles, California. ");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781608866878", "Noelle Stevenson");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781608867370", "Noelle Stevenson");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780062278241", "Noelle Stevenson");
INSERT INTO Writers(WriterName, Gender) VALUES ("Grace Ellis", "Female");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781608866878", "Grace Ellis");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781608867370", "Grace Ellis");

INSERT INTO Illustrators(IllustratorName, Gender, IllustratorImage) VALUES ("Brooke A. Allen", "Female", "model/writers/brooke-allen.jpg");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9781608866878", "Brooke A. Allen");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9781608867370", "Brooke A. Allen");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Young Adult");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608866878", "Slice of Life");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608867370", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608867370", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608867370", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608867370", "Young Adult");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781608867370", "Slice of Life");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781608866878", "Will Eisner Comic Industry Awards for Best New Series & Best Publication for Teens (ages 13-17) (2015)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780062278241", "National Book Award for Young People's Literature (2015)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9780062278241", "Goodreads Choice Awards Best Graphic Novels & Comics (2015)");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780062278241", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780062278241", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780062278241", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780062278241", "Young Adult");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("99780785139546", "Marvel", "2009-03-25",  "Deadpool: Secret Invasion", "299.00", "136", "model/images/99780785139546.jpg", "The Merc with a Mouth is back, even deadlier and more deranged than before! The planet has been invaded by Skrulls, everything's gone topsy-turvy... but, in Deadpool's world, that just means it's Monday! Crazy times call for crazy men, but c'mon, this guy's insane! Like it or not, Deadpool may be the only person on the planet who can save us... but who's to say he wants to? An explosive debut story by writer Daniel Way (Wolverine: Origins, Ghost Rider, Bullseye: Greatest Hits) and fan-favorite artist Paco Medina (New Warriors, New X-Men)! Deadpool: His madness is his method! You won't want to miss it!");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("Daniel Way", "Male", "United States", "model/writers/daniel-way.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("99780785139546", "Daniel Way");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("99780785139546", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("99780785139546", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("99780785139546", "Superhero");

INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780785184027", "Marvel", "2009-03-25",  "Deadpool Killustrated", "299.00", "136", "model/images/9780785184027.jpg", "The Merc with a Mouth is back, even deadlier and more deranged than before! The planet has been invaded by Skrulls, everything's gone topsy-turvy... but, in Deadpool's world, that just means it's Monday! Crazy times call for crazy men, but c'mon, this guy's insane! Like it or not, Deadpool may be the only person on the planet who can save us... but who's to say he wants to? An explosive debut story by writer Daniel Way (Wolverine: Origins, Ghost Rider, Bullseye: Greatest Hits) and fan-favorite artist Paco Medina (New Warriors, New X-Men)! Deadpool: His madness is his method! You won't want to miss it!");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("Cullen Bunn", "Male", "United States", "model/writers/cullen-bun.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780785184027", "Cullen Bunn");
INSERT INTO Illustrators(IllustratorName, Gender) VALUES ("Matteo Lolli", "Male");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9780785184027", "Matteo Lolli");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785184027", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785184027", "Humor");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785184027", "Superhero");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781607066019", "Indigo", "2009-03-25",  "Saga, Volume 1", "299.00", "60", "model/images/9781607066019.jpg", "When two soldiers from opposite sides of a never-ending galactic war fall in love, they risk everything to bring a fragile new life into a dangerous old universe. <br><br>From bestselling writer Brian K. Vaughan, Saga is the sweeping tale of one young family fighting to find their place in the worlds. Fantasy and science fiction are wed like never before in this sexy, subversive drama for adults. ");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781632154385", "Indigo", "2009-03-25",  "Saga, Volume 2", "299.00", "60", "model/images/9781632154385.jpg", "Multiple storylines collide in this cosmos-spanning new volume. While Gwendolyn and Lying Cat risk everything to find a cure for The Will, Marko makes an uneasy alliance with Prince Robot IV to find their missing children, who are trapped on a strange world with terrifying new enemies.");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("Brian K. Vaughan", "Male", "United States", "model/writers/brian-vaughan.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781607066019", "Brian K. Vaughan");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781632154385", "Brian K. Vaughan");

INSERT INTO Illustrators(IllustratorName, Gender, Born, IllustratorImage, IllustratorDescription) VALUES ("Fiona Staples", "Female", "Canada","model/writers/fiona-staples.jpg", "Fiona Staples is a Canadian comic book artist known for her work on books such as North 40, DV8: Gods and Monsters, T.H.U.N.D.E.R. Agents and Saga. She has been cited as one of the best female artists working in the industry, and one of the best artists overall.");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9781607066019", "Fiona Staples");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9781632154385", "Fiona Staples");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781607066019", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781607066019", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781607066019", "Science Fiction");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781632154385", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781632154385", "Fantasy");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781632154385", "Science Fiction");

INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781607066019", "Hugo Award for Best Graphic Story (2013)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781607066019", "Will Eisner Comic Industry Awards for Best New Series, Best Continuing Series, Best Writer (for Brian K. Vaughan) (2013)");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781607066019", "Harvey Awards (2013)");


INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780785190219", "Marvel", "2009-03-25",  "Ms. Marvel, Vol. 1: No Normal", "120.00", "136", "model/images/9780785190219.jpg", "Kamala Khan is an ordinary girl from Jersey City - until she's suddenly empowered with extraordinary gifts. But who truly is the new Ms. Marvel? Teenager? Muslim? Inhuman? Find out as she takes the Marvel Universe by storm! When Kamala discovers the dangers of her newfound powers, she unlocks a secret behind them, as well. Is Kamala ready to wield these immense new gifts? Or will the weight of the legacy before her be too much to bear? Kamala has no idea, either. But she's comin' for you, Jersey!<br><br>It's history in the making from acclaimed writer G. Willow Wilson (Air, Cairo) and beloved artist Adrian Alphona (RUNAWAYS)! Collecting MS. MARVEL (2014) #1-5 and material from ALL-NEW MARVEL NOW! POINT ONE #1.");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780785190226", "Marvel", "2009-03-25",  "Ms. Marvel, Vol. 2: Generation Why", "120.00", "136", "model/images/9780785190226.jpg", "Who is the Inventor, and what does he want with the all-new Ms. Marvel and all her friends? Maybe Wolverine can help! If Kamala can stop fan-girling out about meeting her favorite super hero, that is. Then, Kamala crosses paths with Inhumanity -- by meeting the royal dog, Lockjaw! But why is Lockjaw really with Kamala? As Ms. Marvel discovers more about her past, the Inventor continues to threaten her future. Kamala bands together with some unlikely heroes to stop the maniacal villain before he does real damage, but has she taken on more than she can handle? And how much longer can Ms. Marvel's life take over Kamala Khan's? Kamala Khan continues to prove why she's the best (and most adorable) new super hero there is!");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9780785197362", "Marvel", "2014-03-25",  "Ms. Marvel, Vol. 4: Last Days", "120.00", "136", "model/images/9780785197362.jpg", "When the world is about to end, do you still keep fighting? From the moment, Kamala put on her costume, she's been challenged, but nothing has prepared her for this: the Last Days of the Marvel Universe. Fists up, let's do this, Jersey City. Plus a VERY special guest appearance fans have been clamoring for!");

INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("G. Willow Wilson", "Female", "United States", "model/writers/willow-wilson.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780785190219", "G. Willow Wilson");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780785190226", "G. Willow Wilson");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9780785197362", "G. Willow Wilson");
INSERT INTO Illustrators(IllustratorName, Gender) VALUES ("Adrian Alphona", "Male");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9780785190219", "Adrian Alphona");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9780785190226", "Adrian Alphona");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9780785197362", "Adrian Alphona");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190219", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190219", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190219", "Young Adult");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190226", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190226", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785190226", "Young Adult");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785197362", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785197362", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9780785197362", "Young Adult");

INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781563898686", "DC", "2009-03-25",  "Batman: Dark Victory", "391.00", "136", "model/images/9781563898686.jpg", "The sequel to the critically acclaimed BATMAN: THE LONG HALLOWEEN, DARK VICTORY continues the story of an early time in Batman's life when James Gordon, Harvey Dent, and the vigilante himself were all just beginning their roles as Gotham's protectors.Once a town controlled by organized crime, Gotham City suddenly finds itself being run by lawless freaks, such as Poison Ivy, Mr. Freeze, and the Joker. Witnessing his city's dark evolution, the Dark Knight completes his transformation into the city's greatest defender. He faces multiple threats, including the apparent return of a serial killer called Holiday. Batman's previous investigation of Holiday's killings revealed that more than one person was responsible for the murders. So the question remains: who is committing Holiday's crimes this time? And how many will die before Batman learns the truth?");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("Jeph Loeb", "Male", "United States", "model/writers/jeph-loeb.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781563898686", "Jeph Loeb");
INSERT INTO Illustrators(IllustratorName, Gender) VALUES ("Tim Sale", "Male");
INSERT INTO BookIllustrator(ISBN, IllustratorName) VALUES ("9781563898686", "Jeph Loeb");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781563898686", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781563898686", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781563898686", "Crime Fiction");
INSERT INTO LiteraryAwards(ISBN, Award) Values ("9781563898686", "Will Eisner Comic Industry Awards for Best Graphic Album Reprint (2002) ");

INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781401235444", "DC", "2009-03-25",  "Suicide Squad, Vol. 1: Kicked in the Teeth", "391.00", "136", "model/images/9781401235444.jpg", "As a part of the acclaimed DC Comics--The New 52 event of September 2011, writer and co-creator of the CW show 'Supernatural' Adam Glass rolls out an all-new team of death-row super villains recruited by the government to take on missions so dangerous-they're sheer suicide. <br><br>The story begins with the Suicide Squad defeated, imprisoned and being interrogated about their newest mission. Harley Quinn, King Shark, Deadshot and company must make it out alive without revealing who's pulling the strings behind their illegal operations. Who will be the first to crack under the pressure? More importantly will they make it all out alive? Collects issues #1-7.");
INSERT INTO ComicBooks(ISBN, Publisher, DatePublished, Title, Price, Length, Image, Description) VALUES ("9781401238445", "DC", "2009-03-25",  "Suicide Squad, Vol. 2: Basilisk Rising", "391.00", "136", "model/images/9781401238445.jpg", "As the surviving Squad members attempt to recover from their disastrous Gotham City mission, we learn a dark secret that has been festering in the team since issue #1: a traitor stalks the Suicide Squad! The saboteur's mission: Assassinate Amanda Waller, expose the Squad and leave Task Force X in ruins! The Basilisk strikes! Collects issues #8-13, issue 0, and Resurrection Man #9");
INSERT INTO Writers(WriterName, Gender, Born, WriterImage) VALUES ("Adam Glass", "Male", "United States", "model/writers/adam-glass.jpg");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781401235444", "Adam Glass");
INSERT INTO BookWriter(ISBN, WriterName) VALUES ("9781401238445", "Adam Glass");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401238445", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401238445", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401238445", "Crime Fiction");

INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401235444", "Action/Adventure");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401235444", "Superhero");
INSERT INTO BookGenre(ISBN, Genre) VALUES ("9781401235444", "Crime Fiction")
