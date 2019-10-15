from tracks import *
import urllib.request

with_preview = 0
for i in range(len(tracks_preview)):
    if (tracks_preview[i] != None):
        print(tracks_preview[i])
        preview = urllib.request.urlretrieve(tracks_preview[i], audio_dir + "{0:0=3d}".format(i) + '.mp3')
        with_preview += 1