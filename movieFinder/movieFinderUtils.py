import imdbUtils
import metacriticUtils
import rottenTomatoesUtils
import ytsUtils
from datetime import datetime

newLine = '<br>'
tab = "&nbsp;&nbsp;&nbsp;&nbsp;"

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
	
# Returns a list of various params for the given movies
# Return format is a list of {"movieName":XXX,"genre":GGG,"year":YYYY,"averageRating":RR,"imdbLink":LL} objects
def	getMovieNamesAndAverageRatings(tomatoMoviesInfo):

	moviesList = []

	for movieInfo in tomatoMoviesInfo:
		movieName = movieInfo["movieName"]
		movieTomatoRating = movieInfo["movieRating"]
		movieYear = movieInfo["movieYear"]
		
		imdbRating, genre, imdbLink = imdbUtils.getMovieRatingAndGenre(movieName)
		metacriticRating = metacriticUtils.getMovieRating(movieName)
		averageRating = getAverageRating(imdbRating, movieTomatoRating, metacriticRating)
		
		# DEBUG PRINT - all ratings
		print movieName + "  (" + genre + "," + str(movieYear) + "),  " + "Imdb: ", imdbRating , " Tomato: ", movieTomatoRating, " MetaCritic: ", metacriticRating, " Average:", str(averageRating)
	
		curMovie = {"movieName":movieName,"genre":genre,"year":movieYear,"averageRating":averageRating,"imdbLink":imdbLink}
		moviesList.append(curMovie)
		
	return moviesList


# Returns an email version of the given movies list, which include movie names and their ratings
def getEmailFormatList(moviesList):
	emailMsg = ""
	count = 1

	for movieInfo in moviesList:

		movieLink = "<a href=\"" + movieInfo["imdbLink"] + "\">" + movieInfo["movieName"] + "</a>"
		
		movieLine = str(count) + ") " + movieLink + " (" + movieInfo["genre"] + ")," + tab + "Average Rating: " + str(movieInfo["averageRating"])

		# Look for a torrent link, and add it if found
		torrentLink = ytsUtils.getTorrentLink(movieInfo)
		if (torrentLink <> ""):
			movieLine += tab + "<a href=\"" + torrentLink + "\">torrent</a>"	
		
		emailMsg += movieLine + newLine
		
		count += 1
		
	return emailMsg	

# Returns a plain/text (FOR NOW) mail msg with top movies and ratings	
def getMoviesMail():

	curTime = datetime.now()
	
	moviesEmail = "<h2>This is your MovieMaster update for " + curTime.strftime("%A, %d of %B %Y, %H:%M") + "</h2>"
	
	# Top Box Office Movies
	moviesEmail += "<b> Top Box Office Movies </b>" + newLine
	moviesEmail += "<b> ***************************** </b>" + newLine

	moviesEmail = addMoviesToMail(moviesEmail, rottenTomatoesUtils.getTopBoxOfficeMovies())

	# Top DVD Rentals
	moviesEmail += newLine 
	moviesEmail += "<b> Top DVD Rentals </b> "+ newLine
	moviesEmail += "<b> ********************** </b> " + newLine

	moviesEmail = addMoviesToMail(moviesEmail, rottenTomatoesUtils.getTopDvdRentalsMovies())

	return moviesEmail	
	
# Adds the info for the given movies to the given mail, and returns the updated mail	
def addMoviesToMail(mail, moviesInfo):
	moviesList = getMovieNamesAndAverageRatings(moviesInfo)
	mail += getEmailFormatList(moviesList)
	return mail

