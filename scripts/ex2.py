import subprocess as sp

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

