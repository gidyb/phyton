import urllib
import json

# Returns the id of the first movie on the search result for the given name
#
# IMPORTANT: omdbapi.com is NOT used because it is not up to date.
#
def getMovieId(movieName):
	searchUrl = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + movieName + "&s=all"
	searchPage = urllib.urlopen(searchUrl)
	searchPageHtml = searchPage.read()
	
	findResultIndex = searchPageHtml.index("findResult")
	firstIdIndex = searchPageHtml.index("tt",findResultIndex)
	
	id = searchPageHtml[firstIdIndex:firstIdIndex+9]
	
	return id

	
# Returns the rating of the movie with the given movieId, or "N/A" if the
# movie was not found on IMDB
#
# IMPORTANT: omdbapi.com is NOT used because it is not up to date.
#
def getMovieRating(movieId):
	movieUrl = "http://www.imdb.com/title/" + movieId
	moviePage = urllib.urlopen(movieUrl)
	moviePageHtml = moviePage.read()
	
	ratingStarIndex = moviePageHtml.index("star-box-giga-star")
	ratingIndex = ratingStarIndex + 21
	rating = moviePageHtml[ratingIndex:ratingIndex+3]
	
	return rating
	
# Returns the result of searching IMDB (via omdbapi.com) by movie id using omdbapi.com
#
# omdbapi.com is used here only for getting the movie genre
#
def getMovieById(movieId):
	basicUrl = "http://www.omdbapi.com/?i="
	movieUrl = basicUrl + movieId
	return urllib.urlopen(movieUrl)
	
	
# Returns the IMDB rating, genre and a link to the IMDB movie page of the given movie name 
# in (rating,genre,link) format
#
# ("N/A","N/A","N/A") is returend if the movie was not found on IMDB
#
# The 1st IMDB search result (by movie name) is taken into account
# The rating is on 10-100 scale
def getMovieRatingAndGenre(movieName):	

	# Get first search result movie id
	movieId = getMovieId(movieName)	
	
	# Get movie rating
	try:
		rating = getMovieRating(movieId)
		rating = int(float(rating) * 10)
		moviePageLink = "http://www.imdb.com/title/" + movieId
	except ValueError:
		# Movie was not found on IMDB
		rating = "N/A"
		moviePageLink = "N/A"
	
	# Get movie genre
	idSearchResults = getMovieById(movieId)
	idSearchJson = json.loads(idSearchResults.readline())	
	try:
		genre = idSearchJson['Genre']
	except KeyError:
		genre = "N/A"
	
	return rating,genre,moviePageLink
	
