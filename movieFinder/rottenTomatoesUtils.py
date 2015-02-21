import urllib
import json

# Returns the 10 Top US Box Office movie names and their average
# (critics & audience) ratings
def getTopBoxOfficeMovieNamesAndRatings():
	bestMoviesURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=8b22adt8wam7ned65u2nreqq"
	return getMovieNamesAndRatingsFromJson(bestMoviesURL)	


# Returns the 10 Top US DVD Rentals movie names and their average
# (critics & audience) ratings
def getTopDvdRentalsMovieNamesAndRatings():
	bestDVDsURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=8b22adt8wam7ned65u2nreqq"
	return getMovieNamesAndRatingsFromJson(bestDVDsURL)	
	
	
# Returns the movie names and average ratings from the given RottenTomatoes search URL
def getMovieNamesAndRatingsFromJson(searchURL):
	searchResultsJSON = urllib.urlopen(searchURL)
	movieTitles = json.load(searchResultsJSON)['movies']
	
	movieNamesRatings = {}
	
	for movieInfo in movieTitles:
		averageRating = int((movieInfo['ratings']['critics_score'] + movieInfo['ratings']['audience_score']) / 2)	
		movieNamesRatings[movieInfo['title']] = averageRating
	
	return movieNamesRatings	
	
