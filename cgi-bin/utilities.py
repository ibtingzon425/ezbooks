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

