# Spotify Top 50 Songs - Dataset

BASED ON WORK OF @anxods! 
## What?

- date (Date): when the data is collected (yyyy-mm-dd format)
- position (Integer): the position in the Spotify playlist (1 through 50)
- song (String): name of the song
- artist (String): name of the artist(s) of the song. If several, they will be separated with a &
- popularity (Integer): metric given by Spotify's API to rate how popular a song actually is
- duration_ms (Integer): duration of the song in milliseconds
- album_type (String): single/album...
- total_tracks (Integer): number of tracks in the record
- release_date (Date): when was the song released
- is_explicit (Boolean): True/False
- album_cover_url (String): URL containing the image of the album cover of the song

## When?

The script is set to start executing daily at around 09:15 UTC (11:15 CEST) through an scheduled workflow via Github Workflows, although there may be some delay ([read this for reference](https://www.rockyourcode.com/til-github-actions-on-cron-job-might-be-late/)). 
