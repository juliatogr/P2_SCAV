import subprocess as sp
import ffmpeg

# path to file
bbb = './data/bbb.mp4'

# get the audio format
audio_format = ffmpeg.probe(bbb)["streams"][1]['codec_name']

# now I would try to find the broadcasts standards from
# the audio format but I didn't find how.
