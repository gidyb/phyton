import imdbUtils
import metacriticUtils

# Returns the average of the given movie ratings, ignoring null ratings
def getAverageRating(imdbRating, tomatoesRating, metacriticRating):

	# Tomatoes rating always exists because we take the movie names from there
	validRatings = [tomatoesRating]
		
	# Add non-null ratings to the ratings list
	if (imdbRating <> "N/A"):
		validRatings.append(imdbRating)
	
	if (metacriticRating <> "N/A"):
		validRatings.append(metacriticRating)
	
	return int(sum(validRatings)/len(validRatings))
	

# Prints a list of the given movies, their genre and the average rating between the given
# RottenTomatoes rating and IMDB rating
def printMovieNamesAndAverageRatings(movieNamesAndTomatoesRatings):
	for movie,tomatoesRating in movieNamesAndTomatoesRatings.iteritems():
		imdbRating, genre = imdbUtils.getMovieRatingAndGenre(movie)
		metacriticRating = metacriticUtils.getMovieRating(movie)
		averageRating = getAverageRating(imdbRating, tomatoesRating, metacriticRating)
		
		# DEBUG PRINT - all ratings
		# print movie + "  (" + genre + "),  " + "Imdb: ", imdbRating , " Tomato: ", tomatoesRating, " Meta: ", metacriticRating, " Average:", averageRating
		
		print movie + "  (" + genre + "),  " + "Rating: ", averageRating
		
		
# Prints the given label nicely	
def printLabel(label):
	print "**********************"
	print label
	print "**********************"
	print		
