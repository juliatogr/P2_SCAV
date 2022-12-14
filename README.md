# P2_SCAV

Project to deliver the 2nd laboratory of the video section of Audio and Video Encoding Systems subject 
at Pompeu Fabra University.

## Exercise 1

### Statement

Create a python script able to parse the ‘ffmpeg –i BBB.mp4’ file, 
which can mark at least 3 relevant data from the container

### Solution proposed

printing all metadata from the bbb.mp4 using ffmpeg. 

Code in `ex1.py` script. Execute it in the project folder with the command `python3 scripts/ex1.py`

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

Code in `ex2.py` script. Execute it in the project folder with the command `python3 scripts/ex2.py`

## Exercise 3

### Statement
Create a python script able to resize (resolution change) of any input given

### Solution proposed

The program asks the user the filepath and the new width and height. Then it scales it
to a new output file.

Code in `ex3.py` script. Execute it in the project folder with the command `python3 scripts/ex3.py`

## Exercise 4

### Statement
Create a python script which will check the audio tracks of the video. Then, with this
information, it will explain in which broadcasting standard the video can fit. I.e.: one 
AC-3 audio, that means it can be ATSC.

### Solution proposed

Reads the audio format but I did not finished the exercise because I did not found how to 
get what broadcast standards fit.

Code in `ex4.py` script. Execute it in the project folder with the command `python3 scripts/ex4.py`

## Exercise 5

### Statement
Integrate some or all the previous exercises into one class inside 1 python script.

### Solution proposed

Class Ex5 which has methods for each implemented exercise (1 to 3). The script includes a menu
which lets the user choose the exercise to execute.

Code in `ex5.py` script. Execute it in the project folder with the command `python3 scripts/ex5.py`

## Util links

### Exercise 1
- https://www.streamingmedia.com/Articles/Editorial/Featured-Articles/Discover-the-Six-FFmpeg-Commands-You-Cant-Live-Without-133179.aspx?utm_source=related_articles&utm_medium=gutenberg&utm_campaign=editors_selection
- https://www.thepythoncode.com/article/extract-media-metadata-in-python

### Exercise 2
- https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg
- https://stackoverflow.com/questions/25955322/subprocess-call-ffmpeg-command-line
- https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg
- https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg

### Exercise 3
- https://stackoverflow.com/questions/70797/how-to-prompt-for-user-input-and-read-command-line-arguments
- https://stackoverflow.com/questions/28806816/use-ffmpeg-to-resize-image
- https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
- https://stackoverflow.com/questions/25955322/subprocess-call-ffmpeg-command-line
- https://stackoverflow.com/questions/3476732/how-to-loop-backwards-in-python
