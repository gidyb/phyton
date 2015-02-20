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
	
# Returns the IMDB rating of the given movie name
# The 1st IMDB search result (by movie name) is taken into account
def getMovieRating(movieName):	
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
	ratingIndex = idSearchJson.index("imdbRating")
	return idSearchJson[ratingIndex+13:ratingIndex+16]	
	
