import urllib

TORRENT_LINK_LENGTH = 79

# Returns a torrent download link from yts.to to the given movie, or an empty string if it doesn't exist
def innerGetTorrentLink(movieInfo):

	movieName = movieInfo["movieName"]
	movieYear = movieInfo["year"]

	searchUrl = getSearchUrl(movieName, movieYear)
		
	# Get yts page source
	ytsPage = urllib.urlopen(searchUrl).readline()
	
		
	# Get torrent link (best available quality, which appears last in the page, is taken)
	bestTorrentStartIndex = ytsPage.rfind("http://yts.to/torrent/download")
		
	if (bestTorrentStartIndex == -1):
		print "Could not find " + movieName  + " (" + str(movieYear) + ") torrent on yts.to"
		return "";
	else:
		# Special case - exclude 3D version
		threeDIndex = ytsPage.find("Download 3D", bestTorrentStartIndex)
		if (threeDIndex <> -1):
			bestTorrentStartIndex = ytsPage.rfind("http://yts.to/torrent/download",0,bestTorrentStartIndex - 1)
	
	linkUrl = ytsPage[bestTorrentStartIndex:bestTorrentStartIndex + TORRENT_LINK_LENGTH] 	
	
	print "Found " + movieName + " (" + str(movieYear) + ") torrent on yts.to! Torrent link is: " + linkUrl
	return linkUrl
		
		
# Build yts.to search url for the given movie name and year	
def getSearchUrl(movieName, movieYear):
	ytsMovieNameFormat = ""
	movieName = movieName.replace(':','')
	
	for movieWord in movieName.split():
		ytsMovieNameFormat += movieWord + "-"
	
	return "http://www.yts.to/movie/" + ytsMovieNameFormat + str(movieYear)

def getTorrentLink(movieInfo):

	torrentLink = innerGetTorrentLink(movieInfo)

	# Special case - sometimes the movie appears in yts.to a year before
	if (torrentLink == ""):
		movieInfo["year"] -= 1
		torrentLink = innerGetTorrentLink(movieInfo)
		
	# Just to be sure, search in yts.to for the year after if it wasn't found
	if (torrentLink == ""):
		movieInfo["year"] += 2
		torrentLink = innerGetTorrentLink(movieInfo)
	
	return torrentLink