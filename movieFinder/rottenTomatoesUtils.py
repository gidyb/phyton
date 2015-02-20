import urllib
import json

# Returns the 10 Top US Box Office movie names and their average
# (critics & audience) ratings
def getTopBoxOfficeMovieNamesAndRatings():
	bestMoviesUrl = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=8b22adt8wam7ned65u2nreqq"
	searchResultsJSON = urllib.urlopen(bestMoviesUrl)
		
	movieNamesRatings = {}

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
		
		title = parts[partIndex][titleStartIndex:titleEndIndex]
		rating = getAverageMovieRating(title,parts[partIndex])
		movieNamesRatings[title] = rating
	
	return movieNamesRatings	
	
# Returns the average rating (critics & audience) of the given movie name
# from the given JSON search result	
def getAverageMovieRating(movieName, jsonResult):
	
	# Get critics rating
	criticsRatingIndex = jsonResult.index("critics_score") + 15
	criticsRating = int(jsonResult[criticsRatingIndex : criticsRatingIndex + 2])

	# Get audience rating
	audienceRatingIndex = jsonResult.index("audience_score") + 16
	audienceRating = int(jsonResult[audienceRatingIndex : audienceRatingIndex + 2])

	# Return the average rating
	averageRating = (criticsRating + audienceRating) / 2
	return averageRating
	
	
	
