# P2_SCAV


## Exercise 1

### Statement

Create a python script able to parse the ‘ffmpeg –i BBB.mp4’ file, 
which can mark at least 3 relevant data from the container

### Solution proposed

printing all metadata from the bbb.mp4 using ffmpeg. 

Code in `ex1.py` script.

## Exercise 2

### Statement

You’re going to create a script in order to create a new BBB container:

- Cut BBB into 1 minute only video. 
- Export BBB(1min) audio as MP3 stereo track. 
- Export BBB(1min) audio in AAC w/ lower bitrate

Now package everything in a .mp4 with FFMPEG!!

### Solution proposed

From the `bbb.mp4` video file, export a `bbb_1min.mp4` video, from which I also
export 2 audio files: `bbb_1min_audio.mp3` and `bbb_1min_audio.aac`. Then, I pack
each audio with the extracted video with name indicating the audio format:
`bbb_1min_mp3_pack.mp4` and `bbb_1min_aac_pack.mp4`.

Code in `ex2.py` script inside the `ex2` folder. Execute it in the folder.
Inside the folder there is also an `outputs` folder where there are the mentioned
videos and audios.

## Exercise 3

### Statement
Create a python script able to resize (resolution change) of any input given

### Solution proposed

## Util links

### Exercise 1
- https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Discover-the-Six-FFmpeg-Commands-You-Cant-Live-Without-133179.aspx?utm_source=related_articles&utm_medium=gutenberg&utm_campaign=editors_selection
- https://www.thepythoncode.com/article/extract-media-metadata-in-python

### Exercise 2
- https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg
- https://stackoverflow.com/questions/25955322/subprocess-call-ffmpeg-command-line
- https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg
- https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg