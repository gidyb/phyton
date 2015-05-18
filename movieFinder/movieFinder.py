import movieFinderUtils
import rottenTomatoesUtils
import mailUtils
import time
from datetime import datetime, timedelta

newLine = '\r\n'

mailSender = mailUtils.GmailSender()
mailingList = mailUtils.getMailingList()

while(True):

	for recepient, address in mailingList.iteritems():		
		moviesEmail = "Hello " + recepient + "!" + newLine * 2
		print str(datetime.now()) + "Creating mail"
		moviesEmail = moviesEmail + movieFinderUtils.getMoviesMail()
		print str(datetime.now()) +  "Sending Mail"
		mailSender.send_message(address,"Your MovieFinder Update", moviesEmail)
	
	# Sleep for 1 hour
	time.sleep(3600)
