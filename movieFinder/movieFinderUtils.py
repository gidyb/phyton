import imdbUtils

# Returns 10-100 scale IMDB rating and genre of the given movie
# if the movie has no rating yet (it's too new) - return "N/A" for the rating
def getImdbRatingAndGenre(movie):

	imdbRating, genre = imdbUtils.getMovieRatingAndGenre(movie)
	# Ignore movies with no IMDB rating 
	if (imdbRating <> "N/A") :
		# Convert to 10-100 scale
		imdbRating = float(imdbRating) * 10
	
	return imdbRating, genre
	
	
# Returns the average of the given movie ratings, ignoring null ratings
def getAverageRating(imdbRating, tomatoesRating):
	# Ignore IMDB null ratings 
	if (imdbRating == "N/A"):
		averageRating = tomatoesRating
	else:
		averageRating = (imdbRating + tomatoesRating) / 2
	
	return int(averageRating)
