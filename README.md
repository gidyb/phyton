# Movie Finder

This is a script that periodicaly searches for top movies in RottenTomatoes and sends an email with their names, genres and average ratings from various movie ratings sites (IMDB, RottenTomatoes etc.)

ver 3.0 - Movie Finder is constantly running on an Amazon EC2 instance and sends mails to the given mailing list once a week.

ver 4.0 - Movie Finder is also searching for torrents to the movies it finds on yts.to. A link to the torrent with the best quality (720p, 1080p etc.) is added to the mail, if such torrent exist. Usually, torrents can be found only for top DVD movies and to the top movies in cinema.
