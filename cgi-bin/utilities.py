#!/usr/bin/python


allowedCountries = ['Canada',  'France', 'Japan', 'Philippines', 'Singapore', 'United Kingdom', 'United States']

# Generates the HTML Country Drop Down Element
def generateCountryDropDown(selectedCountry):

	dropDown = '<select name="country"><option value=""></option>'
	
	for country in allowedCountries:
		dropDown = dropDown + '<option value="' + country + '"' 
		if selectedCountry == country :
			dropDown = dropDown + ' selected ' 
		dropDown = dropDown + '>' + country + '</option>'


	dropDown = dropDown + '</select>'	

	return  dropDown

# Generates Book Items Select 
def getBookItems(selectedBooks, cur) :
	bookitems = ""
	command = "SELECT ISBN, Concat(Title, ' (', ISBN, ')') From ComicBooks order by Title;"
	cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
		if row[0] in selectedBooks :
			bookitems = bookitems + '<option value="' + row[0] + '" selected>' + row[1] + '</option>'
		else :	
			bookitems = bookitems + '<option value="' + row[0] + '">' + row[1] + '</option>'
	return bookitems

# Generates Writer Select 
def getWriters(selectedWriters, cur) :
	writers = ""
	command = "SELECT WriterName From Writers order by WriterName;"
	cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
		if row[0] in selectedWriters:
			writers= writers + '<option value="' + row[0] + '" selected>' + row[0] + '</option>'
		else :	
			writers = writers + '<option value="' + row[0] + '">' + row[0] + '</option>'
	return writers

def getIllustrators(selectedIllustrators, cur) :
	illustrators = ""
	command = "SELECT IllustratorName From Illustrators order by IllustratorName;"
	cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
		if row[0] in selectedIllustrators:
			illustrators= illustrators + '<option value="' + row[0] + '" selected>' + row[0] + '</option>'
		else :	
			illustrators = illustrators + '<option value="' + row[0] + '">' + row[0] + '</option>'
	return illustrators

def getGenres(selectedGenre, cur) :
	genre = ""
	command = "SELECT Genre From Genres order by Genre;"
	cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
		if row[0] in selectedGenre:
			genre= genre + '<option value="' + row[0] + '" selected>' + row[0] + '</option>'
		else :	
			genre = genre + '<option value="' + row[0] + '">' + row[0] + '</option>'
	return genre

# Initializes Side Bar objects
def getSideBar(email, isAdministrator, cur) :
	sidebar = {'genres':[], 'publishers':[], 'users':'', 'writers':'', 'illustrators':'', 'books':''}

	# Get Genres
	command = "select Genre FROM Genres order by Genre"
	cur.execute(command)
	rows = cur.fetchall()
	for row in rows:
		if row[0] not in sidebar['genres']:
			sidebar['genres'].append(row[0])

	command = "select distinct Publisher from ComicBooks order by Publisher"
	cur.execute(command)
	rows = cur.fetchall()
	for row in rows:
		if row[0] not in sidebar['publishers']:
			sidebar['publishers'].append(row[0])

	if isAdministrator == "Y":
		# Get Books
                sidebar['books'] = ''
                command = "select ISBN, Concat(Title, ' (', ISBN, ')') From ComicBooks order by Title;"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['books'] = sidebar['books'] + '<li><a href="comic-book-item.py?ISBN=' + str(row[0]) + '">'+ row[1] +'</a></li>'


		# Get Genres
		sidebar['genres-dd'] = '' 
		command = "select Genre FROM Genres order by Genre"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['genres-dd'] = sidebar['genres-dd'] + '<li><a href="home.py?genre=' + row[0] + '">'+ row[0] +'</a></li>'		

		# Get Illustrators
		command = "select IllustratorName from Illustrators order by IllustratorName"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['illustrators'] = sidebar['illustrators'] + '<li><a href="illustrator-profile.py?illustrator=' + str(row[0]) + '">'+ row[0] +'</a></li>'


		# Get Writers
		command = "select WriterName from Writers order by WriterName"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['writers'] = sidebar['writers'] + '<li><a href="writer-profile.py?writer=' + str(row[0]) + '">'+ row[0] +'</a></li>'

		# Get Users
		command = "select Email, CONCAT(FirstName, ' ', LastName, ' (',  Email, ')')   from Users order by FirstName, LastName;"
		cur.execute(command)
                rows = cur.fetchall()
		for row in rows:
			sidebar['users'] = sidebar['users'] + '<li><a href="user-profile.py?user=' + row[0] + '">'+ row[1] +'</a></li>'
	
	return sidebar;


