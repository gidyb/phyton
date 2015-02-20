import urllib

# Returns the result of searching IMDB by movie name
def getImdbSearchResults(movieName):
	basicUrl = "http://www.omdbapi.com/?s="
	movieUrl = basicUrl + movieName
	return urllib.urlopen(movieUrl)

# Returns the result of searching IMDB by movie id
def getImdbByMovieId(movieId):
	basicUrl = "http://www.omdbapi.com/?i="
	movieUrl = basicUrl + movieId
	return urllib.urlopen(movieUrl)

# Returns the movie genre from the given json search result of a movie
def getMovieGenre(jsonMovie):
	genreStartIndex = jsonMovie.index("Genre") + 8
	genreEndIndex = jsonMovie.index("Director") - 3
	genre = jsonMovie[genreStartIndex:genreEndIndex]
	return genre	

# Return the movie rating from the given json search result of a movie	
def getMovieRating(jsonMovie):
	ratingIndex = jsonMovie.index("imdbRating")
	return jsonMovie[ratingIndex+13:ratingIndex+16]	
	
	
# Returns the IMDB rating and genre of the given movie name in (rating,genre) format
#
# The 1st IMDB search result (by movie name) is taken into account
# The rating is on 1-10 scale
def getMovieRatingAndGenre(movieName):	
	# Get first movie id 			
	titleSearchResults = getImdbSearchResults(movieName)
	searchJson = titleSearchResults.readline()
	
	try:
		firstIdIndex = searchJson.index("tt")
	except ValueError:
		# Search returned no movies
		print "There are no movies named" , movieName
		return -1
		
	movieId = searchJson[firstIdIndex:firstIdIndex+9]

	# Get movie Rating
	idSearchResults = getImdbByMovieId(movieId)
	idSearchJson = idSearchResults.readline()
	
	rating = getMovieRating(idSearchJson)
	genre = getMovieGenre(idSearchJson)
	return rating,genre
	
