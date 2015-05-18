import urllib
import json

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

# Returns the IMDB rating (if such exists, 'N/A' otherwise) and genre of the given movie name in (rating,genre) format
#
# The 1st IMDB search result (by movie name) is taken into account
# The rating is on 10-100 scale
def getMovieRatingAndGenre(movieName):	
	# Get first movie id 			
	titleSearchResults = getImdbSearchResults(movieName)
	searchJson = titleSearchResults.readline()
	
	try:
		firstIdIndex = searchJson.index("tt")
	except ValueError:
		# Search returned no movies
		print "There are no movies named" , movieName
		return -1, "None"
		
	movieId = searchJson[firstIdIndex:firstIdIndex+9]

	# Get movie Rating
	idSearchResults = getImdbByMovieId(movieId)
	idSearchJson = json.loads(idSearchResults.readline())
	
	try:
		rating = idSearchJson['imdbRating']
	except KeyError:
		return -1,"None"
		
	if (rating <> 'N/A'):
		rating = int(float(rating) * 10)
		
	genre = idSearchJson['Genre']
	
	return rating,genre
	
