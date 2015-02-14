import imdbUtils
import rottenTomatoesUtils

topBoxOfficeMovies = rottenTomatoesUtils.getTopBoxOfficeMovies()

for movie in topBoxOfficeMovies:

	movieRating = imdbUtils.getMovieRating(movie)
	print movie, movieRating
