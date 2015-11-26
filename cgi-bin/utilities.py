#!/usr/bin/python


allowedCountries = ['Canada', 'England', 'France', 'Japan', 'Philippines', 'Singapore', 'United States']

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
	command = "select ISBN, Concat(Title, ' (', ISBN, ')') From ComicBooks order by Title;"
	cur.execute(command)
        rows = cur.fetchall()
        for row in rows:
		if row[0] in selectedBooks :
			bookitems = bookitems + '<option value="' + row[0] + '" selected>' + row[1] + '</option>'
		else :	
			bookitems = bookitems + '<option value="' + row[0] + '">' + row[1] + '</option>'
	return bookitems


# Initializes Side Bar objects
def getSideBar(email, isAdministrator, cur) :
	sidebar = {'genres':[], 'publishers':[], 'users':'', 'writers':'', 'illustrators':'', 'books':''}

	if isAdministrator == "N":

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
	else :
		# Get Books
                sidebar['books'] = ''
                command = "select ISBN, Concat(Title, ' (', ISBN, ')') From ComicBooks order by Title;"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['books'] = sidebar['books'] + '<li><a href="comic-book-item.py?email=' + email + '&ISBN=' + str(row[0]) + '">'+ row[1] +'</a></li>'


		# Get Genres
		sidebar['genres'] = '' 
		command = "select Genre FROM Genres order by Genre"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['genres'] = sidebar['genres'] + '<li><a href="home.py?email=' + email + '&genre=' + row[0] + '">'+ row[0] +'</a></li>'		

		# Get Illustrators
		command = "select IllustratorId, IllustratorName from Illustrators order by IllustratorName"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['illustrators'] = sidebar['illustrators'] + '<li><a href="illustrator-profile.py?email=' + email + '&illustrator=' + str(row[0]) + '">'+ row[1] +'</a></li>'


		# Get Writers
		command = "select WriterId, WriterName from Writers order by WriterName"
                cur.execute(command)
                rows = cur.fetchall()
                for row in rows:
                        sidebar['writers'] = sidebar['writers'] + '<li><a href="writer-profile.py?email=' + email + '&writer=' + str(row[0]) + '">'+ row[1] +'</a></li>'

		# Get Users
		command = "select Email, CONCAT(FirstName, ' ', LastName, ' (',  Email, ')')   from Users order by FirstName, LastName;"
		cur.execute(command)
                rows = cur.fetchall()
		for row in rows:
			sidebar['users'] = sidebar['users'] + '<li><a href="user-profile.py?email=' + email + '&user=' + row[0] + '">'+ row[1] +'</a></li>'
	

	return sidebar;


