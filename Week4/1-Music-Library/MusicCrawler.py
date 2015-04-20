from __future__ import print_function
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import TIT2
from mutagen.id3 import TALB
import os
import datetime
from Song import Song
from Playlist import Playlist



class MusicCrawler():

    def __init__(self, dirpath):
        if os.path.isdir(dirpath) == False:
            raise AttributeError("No such directory !")
        self._dirpath = dirpath
        os.chdir(self._dirpath)

    def generate_playlist(self):
        returnPl = Playlist()
        for file in os.listdir(self._dirpath):
            if file.endswith(".mp3"):
                song = MP3(file, ID3=EasyID3)
                #print(song["title"][0].decode("utf-8"))
                returnPl.add_song(Song(song["title"][0], song["artist"][0], song["album"][0], str(datetime.timedelta(seconds=int(song.info.length)))))
        return returnPl

mc = MusicCrawler("/home/george/Music")
playlist = mc.generate_playlist()
playlist.pprint_playlist()

playlist.artists()

print(playlist.total_length())
playlist.save()
