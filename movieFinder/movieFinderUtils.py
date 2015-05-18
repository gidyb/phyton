import imdbUtils
import metacriticUtils
import rottenTomatoesUtils
from datetime import datetime

newLine = '\r\n'

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
	

# Prints a list of the given movies, their genre and the average rating between various sites
# Needed for the CMD version - MovieFinder
def printMovieNamesAndAverageRatings(movieNamesAndTomatoesRatings):
	for movie,tomatoesRating in movieNamesAndTomatoesRatings.iteritems():
		imdbRating, genre = imdbUtils.getMovieRatingAndGenre(movie)
		metacriticRating = metacriticUtils.getMovieRating(movie)
		averageRating = getAverageRating(imdbRating, tomatoesRating, metacriticRating)
		
		# DEBUG PRINT - all ratings
		print movie + "  (" + genre + "),  " + "Imdb: ", imdbRating , " Tomato: ", tomatoesRating, " MetaCritic: ", metacriticRating, " Average:", averageRating
		
		print movie + "  (" + genre + "),  " + "Rating: ", averageRating
	
		
# Prints the given label nicely	to the cmd
def printLabel(label):
	print "**********************"
	print label
	print "**********************"
	print		
	

# Returns a list of the given movies, their genre and the average rating between various sites
# Needed for the Server version - MovieMaster	
def	getMovieNamesAndAverageRatings(movieNamesAndTomatoesRatings):

	moviesList = []

	for movie,tomatoesRating in movieNamesAndTomatoesRatings.iteritems():
		imdbRating, genre = imdbUtils.getMovieRatingAndGenre(movie)
		metacriticRating = metacriticUtils.getMovieRating(movie)
		averageRating = getAverageRating(imdbRating, tomatoesRating, metacriticRating)
		
		# DEBUG PRINT - all ratings
		print movie + "  (" + genre + "),  " + "Imdb: ", imdbRating , " Tomato: ", tomatoesRating, " MetaCritic: ", metacriticRating, " Average:", averageRating
	
		movieLine = movie + "  (" + genre + "),  " + "Rating: " + str(averageRating)	
		moviesList.append(movieLine)

	return moviesList
	
	
# Returns an email version of the given movies list, which include movie names and their ratings
def getEmailFormatList(moviesList):
	emailMsg = ""

	for movie in moviesList:
		emailMsg = emailMsg + movie + newLine
		
	return emailMsg	

# Returns a plain/text (FOR NOW) mail msg with top movies and ratings	
def getMoviesMail():

	curTime = datetime.now()
	
	moviesEmail = "This is your MovieMaster update for " + curTime.strftime("%A, %d of %B %Y, %H:%M") + newLine * 2
	
	# Top Box Office Movies
	moviesEmail = moviesEmail + "Top Box Office Movies" + newLine
	moviesEmail = moviesEmail + "*************************" + newLine

	topBoxOffice = rottenTomatoesUtils.getTopBoxOfficeMovieNamesAndRatings()
	moviesList = getMovieNamesAndAverageRatings(topBoxOffice)
	moviesEmail = moviesEmail + getEmailFormatList(moviesList)

	# Top DVD Rentals
	moviesEmail = moviesEmail + newLine 
	moviesEmail = moviesEmail + "Top DVD Rentals" + newLine
	moviesEmail = moviesEmail + "*******************" + newLine

	topDVDs = rottenTomatoesUtils.getTopDvdRentalsMovieNamesAndRatings()
	dvdsList = getMovieNamesAndAverageRatings(topDVDs)
	moviesEmail = moviesEmail + getEmailFormatList(dvdsList)

	return moviesEmail	
