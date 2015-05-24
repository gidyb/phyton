import urllib
import json

# Returns the 10 Top US Box Office movie names and their average
# (critics & audience) ratings
def getTopBoxOfficeMovies():
	bestMoviesURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/box_office.json?apikey=8b22adt8wam7ned65u2nreqq"
	return getMoviesInfoFromJson(bestMoviesURL)	


# Returns the 10 Top US DVD Rentals movie names and their average
# (critics & audience) ratings
def getTopDvdRentalsMovies():
	bestDVDsURL = "http://api.rottentomatoes.com/api/public/v1.0/lists/dvds/top_rentals.json?apikey=8b22adt8wam7ned65u2nreqq"
	return getMoviesInfoFromJson(bestDVDsURL)	
	
	
# Returns the movie names and average ratings from the given RottenTomatoes search URL
# Return format is a list of {"movieName":XXX,"movieRating":RR,"movieYear":YYYY} objects
def getMoviesInfoFromJson(searchURL):
	searchResultsJSON = urllib.urlopen(searchURL)
	movieTitles = json.load(searchResultsJSON)['movies']
	
	moviesInfo = []

	for movieInfo in movieTitles:
		averageRating = int((movieInfo['ratings']['critics_score'] + movieInfo['ratings']['audience_score']) / 2)	
		curMovieInfo = {"movieName":movieInfo['title'], "movieRating":averageRating, "movieYear":movieInfo['year']}
		moviesInfo.append(curMovieInfo)

	
	return moviesInfo	
	
