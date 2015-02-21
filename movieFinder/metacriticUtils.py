import unirest
import json

# Returns the given movie rating from Metacritic site (10-100 scale)
# Returns "N/A" if the movie was not found
def getMovieRating(movieName):
	
	jsonResponse = unirest.post("https://byroredux-metacritic.p.mashape.com/find/movie",
		  headers={
		  	"X-Mashape-Key": "0iV8kx3KKImshC2cnis7clmXp7jKp1hQ6yBjsn2FPx4lkK7rB9",
			  "Content-Type": "application/x-www-form-urlencoded",
			  "Accept": "application/json"
		  },
		  params={
			  "retry": 4,
			  "title": movieName
		  }
		)
	
	
	result = jsonResponse.body['result']
	
	if (result):
		return int(float(result['userscore']) * 10)	
	else:
		return "N/A"
