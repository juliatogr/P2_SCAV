import ffmpeg
from pprint import pprint

# path to file
bbb = './data/bbb.mp4'

# pprint for printing Python dictionaries in a human-readable way
# probe gets de metadata streams of the multimedia file
pprint(ffmpeg.probe(bbb)["streams"])
