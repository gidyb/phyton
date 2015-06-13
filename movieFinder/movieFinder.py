import movieFinderUtils
import rottenTomatoesUtils
import mailUtils
import time
from datetime import datetime, timedelta

newLine = '<br>'

mailSender = mailUtils.GmailSender()

while(True):

	# Compute movies
	print str(datetime.now()) + ": Building Movie Mail"
	moviesPart = movieFinderUtils.getMoviesMail()

	# Send to all mailing list
	for recepient in mailUtils.getMailingList():
		print str(datetime.now()) +  ": Sending Mail to: " + recepient["name"]
		moviesEmail = "<h1> Hello " + recepient["name"] + "! </h1>"
		moviesEmail = moviesEmail + moviesPart
		mailSender.send_message(recepient["email"],"Your MovieMaster Update", moviesEmail)
	
	# Sleep for 7 days
	time.sleep(604800)
	
