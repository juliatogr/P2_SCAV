import subprocess as sp

# ask for the parameters
file = input("Please enter the path to the input file. (Ex. ../data/bbb.mp4) ")
w = input("Please enter the desired width. (Ex. 320) ")
h = input("Please enter the desired height. (Ex. 240) ")

# Get the format of the file
file_format = ""

for i in range(len(file), 0, -1):
    file_format = file[i-1] + file_format
    if file[i-1] == ".":
        break

# change the scale of the input
sp.call([
    'ffmpeg',
    '-i', file,
    '-vf', 'scale=%sx%s' % (w, h),
    './outputs/output_%sx%s%s' % (w, h, file_format)
])
