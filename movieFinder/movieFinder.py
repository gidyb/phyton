import rottenTomatoesUtils
import movieFinderUtils

# Get the names of the current 10 top box office movies from RottenTomatoes
topBoxOfficeMoviesAndRatings = rottenTomatoesUtils.getTopBoxOfficeMovieNamesAndRatings()

# Print a nice label
print "**********************"
print "Top Box Office Movies:"
print "**********************"
print

# For each movie, get the genre and the average rating on IMDB and RottenTomatoes
for movie,tomatoesRating in topBoxOfficeMoviesAndRatings.iteritems():

	imdbRating, genre = movieFinderUtils.getImdbRatingAndGenre(movie)
	
	print movie + "  (" + genre + "),  " + "Rating: ", movieFinderUtils.getAverageRating(imdbRating, tomatoesRating)

	
# Wait for input so that the cmd window won't close	
print
var = raw_input("Press any key to continue...")



