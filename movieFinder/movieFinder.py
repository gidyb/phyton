import rottenTomatoesUtils
import movieFinderUtils

def printLabel(label):
	print "**********************"
	print label
	print "**********************"
	print

# Prints a list of the given movies, their genre and the average rating between the given
# RottenTomatoes rating and IMDB rating
def printMovieNamesAndAverageRatings(movieNamesAndTomatoesRatings):
	for movie,tomatoesRating in movieNamesAndTomatoesRatings.iteritems():
		imdbRating, genre = movieFinderUtils.getImdbRatingAndGenre(movie)
		print movie + "  (" + genre + "),  " + "Rating: ", movieFinderUtils.getAverageRating(imdbRating, tomatoesRating)
		


# Top Box Office movies
#***********************
topBoxOfficeMoviesAndRatings = rottenTomatoesUtils.getTopBoxOfficeMovieNamesAndRatings()
printLabel("Top Box Office Movies:")
printMovieNamesAndAverageRatings(topBoxOfficeMoviesAndRatings)

print
print

# Top DVD Rentals movies
#***********************
topDvdRentalsAndRatings = rottenTomatoesUtils.getTopDvdRentalsMovieNamesAndRatings()
printLabel("Top DVD Rentals Movies:")
printMovieNamesAndAverageRatings(topDvdRentalsAndRatings)

	
# Wait for input so that the cmd window won't close	
print
var = raw_input("Press any key to continue...")



