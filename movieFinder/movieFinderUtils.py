import imdbUtils
import metacriticUtils
import rottenTomatoesUtils
import ytsUtils
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
	
# Prints the given label nicely	to the cmd
def printLabel(label):
	print "**********************"
	print label
	print "**********************"
	print		
	

# Returns a list of the given movies, their genre and the average rating between various sites
# Return format is a list of {"movieName":XXX,"genre":GGG,"year":YYYY,"averageRating":RR} objects
def	getMovieNamesAndAverageRatings(tomatoMoviesInfo):

	moviesList = []

	for movieInfo in tomatoMoviesInfo:
		movieName = movieInfo["movieName"]
		movieTomatoRating = movieInfo["movieRating"]
		movieYear = movieInfo["movieYear"]
		
		imdbRating, genre = imdbUtils.getMovieRatingAndGenre(movieName)
		metacriticRating = metacriticUtils.getMovieRating(movieName)
		averageRating = getAverageRating(imdbRating, movieTomatoRating, metacriticRating)
		
		# DEBUG PRINT - all ratings
		print movieName + "  (" + genre + "," + str(movieYear) + "),  " + "Imdb: ", imdbRating , " Tomato: ", movieTomatoRating, " MetaCritic: ", metacriticRating, " Average:", str(averageRating)
	
		curMovie = {"movieName":movieName,"genre":genre,"year":movieYear,"averageRating":averageRating}
		moviesList.append(curMovie)
		
	return moviesList


# Returns an email version of the given movies list, which include movie names and their ratings
def getEmailFormatList(moviesList):
	emailMsg = ""

	for movieInfo in moviesList:

		torrentLink = ytsUtils.getTorrentLink(movieInfo)
		
		movieLine = movieInfo["movieName"] + " (" + movieInfo["genre"] + "),  " + "Rating: " + str(movieInfo["averageRating"]) + newLine
		movieLine += "Torrent: " + torrentLink + newLine
		emailMsg += movieLine + newLine
		
	return emailMsg	

# Returns a plain/text (FOR NOW) mail msg with top movies and ratings	
def getMoviesMail():

	curTime = datetime.now()
	
	moviesEmail = "This is your MovieMaster update for " + curTime.strftime("%A, %d of %B %Y, %H:%M") + newLine * 2
	
	# Top Box Office Movies
	moviesEmail += "Top Box Office Movies" + newLine
	moviesEmail += "*************************" + newLine

	moviesEmail = addMoviesToMail(moviesEmail, rottenTomatoesUtils.getTopBoxOfficeMovies())

	# Top DVD Rentals
	moviesEmail += newLine 
	moviesEmail += "Top DVD Rentals" + newLine
	moviesEmail += "*******************" + newLine

	moviesEmail = addMoviesToMail(moviesEmail, rottenTomatoesUtils.getTopDvdRentalsMovies())

	return moviesEmail	
	
# Adds the info for the given movies to the given mail, and returns the updated mail	
def addMoviesToMail(mail, moviesInfo):
	moviesList = getMovieNamesAndAverageRatings(moviesInfo)
	mail += getEmailFormatList(moviesList)
	return mail

