import urllib
import json

def getTopBoxOfficeMovies():
	bestMoviesUrl = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=8b22adt8wam7ned65u2nreqq"
	searchResultsJSON = urllib.urlopen(bestMoviesUrl)
		
	return getMovieTitles(searchResultsJSON)
	

		
def getMovieTitles(searchResultsJSON):
	
	movieTitles = []

	# Pass empty lines
	lineStr = searchResultsJSON.readline().strip()
	while (not lineStr):
		lineStr = searchResultsJSON.readline().strip()
	
	# Find movie titles
	parts = lineStr.split("title")
	for partIndex in range(1,11):
	
		titleStartIndex = 3
		
		try:
			titleEndIndex = parts[partIndex].index("year") - 3
		except ValueError:
		# There is no year in the movie
			continue;
			
		movieTitles.append(parts[partIndex][titleStartIndex:titleEndIndex])
		
	return movieTitles	
		
