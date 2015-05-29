import smtplib

class GmailSender(object):
	
    def createSession(self):
        self.email = "gidysmoviemaster@gmail.com"
        self.password = "moviemaster123"
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, addressTo, subject, body):
		# Create new SMTP session each time to avoid SMTPServerDisconnect exception (while idle)
		self.createSession()
		
		# Prepare msg
		headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + addressTo,
            "MIME-Version: 1.0",
           "Content-Type: text/plain"]
		headers = "\r\n".join(headers)
		self.session.sendmail(
            self.email,
            addressTo,
            headers + "\r\n\r\n" + body)
			


def getMailingList():
	mailingList = {}
	
	mailingList["Gidy"] = "gidy.basin@gmail.com"
	# More users....
	
	return mailingList
