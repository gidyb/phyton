import rottenTomatoesUtils
import movieFinderUtils

# Top Box Office movies
#***********************
topBoxOfficeMoviesAndRatings = rottenTomatoesUtils.getTopBoxOfficeMovieNamesAndRatings()
movieFinderUtils.printLabel("Top Box Office Movies:")
movieFinderUtils.printMovieNamesAndAverageRatings(topBoxOfficeMoviesAndRatings)

print
print

# Top DVD Rentals movies
#***********************
topDvdRentalsAndRatings = rottenTomatoesUtils.getTopDvdRentalsMovieNamesAndRatings()
movieFinderUtils.printLabel("Top DVD Rentals Movies:")
movieFinderUtils.printMovieNamesAndAverageRatings(topDvdRentalsAndRatings)

	
# Wait for input so that the cmd window won't close	
print
var = raw_input("Press any key to continue...")
