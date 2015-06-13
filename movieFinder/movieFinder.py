import movieFinderUtils
import rottenTomatoesUtils
import mailUtils
import time
from datetime import datetime, timedelta

newLine = '\r\n'

mailSender = mailUtils.GmailSender()

while(True):

	for recepient in mailUtils.getMailingList():
		moviesEmail = "Hello " + recepient["name"] + "!" + newLine * 2
		print str(datetime.now()) + ": Creating mail"
		moviesEmail = moviesEmail + movieFinderUtils.getMoviesMail()
		print str(datetime.now()) +  ": Sending Mail"
		mailSender.send_message(recepient["email"],"Your MovieFinder Update", moviesEmail)
	
	# Sleep for 7 days
	time.sleep(604800)
	

