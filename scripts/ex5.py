import subprocess as sp
import ffmpeg
from pprint import pprint


class Ex5(object):

    @classmethod
    def ex1(cls):
        # path to file
        bbb = './data/bbb.mp4'

        # pprint for printing Python dictionaries in a human-readable way
        # probe gets de metadata streams of the multimedia file
        pprint(ffmpeg.probe(bbb)["streams"])

    @classmethod
    def ex2(cls):
        # cut the original video to a 1-minute video

        sp.call([
            'ffmpeg',
            '-i', './data/bbb.mp4',
            '-ss', '00:00:00',
            '-t', '00:01:00',
            '-c:v', 'copy',
            './outputs/ex2/bbb_1min.mp4',
        ])

        sp.call([
            'ffmpeg',
            '-i', './outputs/ex2/bbb_1min.mp4',
            '-q:a', '0',
            '-map', 'a',
            './outputs/ex2/bbb_1min_audio.mp3'
        ])

        sp.call([
            'ffmpeg',
            '-i', './outputs/ex2/bbb_1min.mp4',
            '-q:a', '0',
            '-map', 'a',
            '-b:a', '256k',
            './outputs/ex2/bbb_1min_audio.aac'
        ])

        sp.call([
            'ffmpeg',
            '-i', './outputs/ex2/bbb_1min.mp4',
            '-i', './outputs/ex2/bbb_1min_audio.mp3',
            '-c:v', 'copy',
            '-c:a', 'aac',
            './outputs/ex2/bbb_1min_mp3_pack.mp4'
        ])

        sp.call([
            'ffmpeg',
            '-i', './outputs/ex2/bbb_1min.mp4',
            '-i', './outputs/ex2/bbb_1min_audio.aac',
            '-c:v', 'copy',
            '-c:a', 'aac',
            './outputs/ex2/bbb_1min_aac_pack.mp4'
        ])

    @classmethod
    def ex3(cls):
        # ask for the parameters
        file = input(
            "Please enter the path to the input file. (Ex. ./data/bbb.mp4) ")
        w = input("Please enter the desired width. (Ex. 320) ")
        h = input("Please enter the desired height. (Ex. 240) ")

        # Get the format of the file
        file_format = ""

        for i in range(len(file), 0, -1):
            file_format = file[i - 1] + file_format
            if file[i - 1] == ".":
                break

        # change the scale of the input
        sp.call([
            'ffmpeg',
            '-i', file,
            '-vf', 'scale=%sx%s' % (w, h),
                   './outputs/ex3/output_%sx%s%s' % (w, h, file_format)
        ])


ex = Ex5()

exit_app = False

while not exit_app:

    opt = int(input(
        "Please enter the number of the exercise you want to execute [1-3]. \n"
        "0 to exit.\n"))

    if opt == 1:
        ex.ex1()
    elif opt == 2:
        ex.ex2()
    elif opt == 3:
        ex.ex3()
    elif opt == 0:
        exit_app = True
        print("bye")
    else:
        print("incorrect option")



