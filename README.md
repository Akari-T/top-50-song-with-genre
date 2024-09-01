# \[Modified Fork Project\] Spotify Top 50 Songs 

**Quick Overview** A mini-Spotify-project, based on [@anxods](https://github.com/anxods/spotify-top-50-songs/tree/main?tab=readme-ov-file)'s wonderful work! 

**Motivation** To learn data retrieval through APIs, setting up GitHub workflow and gaining more practice with GitHub. 

------

This project is a modified fork of anxods's [Spotify Top 50 Songs - Dataset](https://github.com/anxods/spotify-top-50-songs/tree/main?tab=readme-ov-file). 
While most of the code comes from the original projects, I have made the following modifications: 

- Removed Spain, Mexico, Argentina and added China, Germany, India, Brazil, Canada.
- Removed *total_tracks* and added *genre_list* and *uri*.
  - Since Spotify does not provide genres for each song, the artist(s)'s genres were used in place. Therefore, the genre may not be reflective of the song itself.
- Updated GitHub Action versions.
- Scheduled the script to run at 04:42 UTC (21:42 PT) through GitHub Workflow (still confirming that it runs correctly). 
