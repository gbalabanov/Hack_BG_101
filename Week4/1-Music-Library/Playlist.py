from Song import Song
import json
import re
import random


class Playlist:

    def __init__(self, name="Code", repeat=False, shuffle=False):
        self._name = name
        self._repeat = repeat
        self._shuffle = shuffle
        self.songs = []
        self.currentsong = -1
        self.shuffledsongs = []

    def add_song(self, item):
        if isinstance(item, Song) and item not in self.songs:
            self.songs.append(item)
        else:
            return "Fail !"

    def add_songs(self, lst):
        if not isinstance(lst, list):
            return "Check your list !"
        for x in lst:
            if not isinstance(x, Song):
                continue
            else:
                self.add_song(x)
        if self._shuffle == True:
            templist=[]
            for x in self.songs:
                templist.append(x)
            random.shuffle(templist)
            self.shuffledsongs = templist


    def pprint_playlist(self):
        maxArtist = 0
        maxTitle = 0
        maxLength = 0
        for x in self.songs:
            if len(x._title) > maxTitle:
                maxTitle = len(x._title)
            if len(x._artist) > maxArtist:
                maxArtist = len(x._artist)
            if maxArtist < 5:
                maxArtist = 5
            if maxTitle < 5:
                maxTitle = 5
            if len(x._length) > maxLength:
                maxLength = len(x._length)
            if maxLength < 5:
                maxLength = 5
        print("| Artist " + " " * (maxArtist - 5) +
              "| Song" + " " * (maxTitle - 3) + "| Length " + " " * (maxLength - 5) + "|")
        print("-" * (12 + maxArtist + maxTitle + maxLength))
        for x in self.songs:
            print("| " + x._artist + " " * (maxArtist - len(x._artist) + 2) + "| " + x._title + " " * (maxTitle - len(x._title) + 1)) + "| " + x._length + " " * (maxLength - len(x._length) + 2) + "|"
        print("")

    def total_length(self):
        totalsecs = 0
        timelist = {}
        output = ""
        for x in self.songs:
            totalsecs += x.length(True)
        for x in range(2, -1, -1):
            if totalsecs / 60**x == 0:
                timelist[x] = 0
                continue
            else:
                if x == 0:
                    timelist[x] = totalsecs
                else:
                    timelist[x] = totalsecs // 60**x
                    totalsecs %= 60**x
        for x in timelist:
            output += str(x) + ":"
        return "{:02}:{:02}:{:02}".format(timelist[2], timelist[1],  timelist[0])

    def artists(self):
        artist = set()
        output = {}
        for x in self.songs:
            artist.add(x._artist)
        for x in artist:
            output[x] = 0
        for x in self.songs:
            if x._artist in output.keys():
                output[x._artist] += 1
        print(output)

    def save(self):
        pl_name = self._name.replace(" ", "-")
        fl_name = self._name.replace(" ", "-") + ".json"
        with open(fl_name, "w") as f:
            f.writelines(json.dumps(pl_name) + "\n")
            for x in self.songs:
                f.write(json.dumps(repr(x)) + "\n")

    @staticmethod
    def load(filename):
        output = Playlist("")
        song_atr = []
        with open(filename, "r") as f:
            output._name = f.readline().replace("-", " ")
            for line in f:
                song_atr.append(line.split(","))
            for x in song_atr:
                x[3] = re.sub("\D{1,2}$", "", x[3])
                output.songs.append(
                    Song(x[0].strip("\""), x[1].strip(), x[2].strip(), x[3].strip()))
        return output

    def next_song(self):
        if self._repeat == False and self._shuffle == False:
            self.currentsong += 1

            if self.currentsong >= len(self.songs):
                return "End of playlist !"

            return self.songs[self.currentsong]
        if self._repeat == True and self._shuffle == False:
            self.currentsong += 1

            if self.currentsong >= len(self.songs):
                self.currentsong = 0

            return self.songs[self.currentsong]

        if self._repeat == True and self._shuffle == True:
            self.currentsong += 1

            if self.currentsong >= len(self.songs):
                self.currentsong = 0

            return self.shuffledsongs[self.currentsong]

        if self._repeat == False and self._shuffle == True:
            self.currentsong += 1

            if self.currentsong >= len(self.songs):
                return "End of playlist !"

            return self.shuffledsongs[self.currentsong]


#a = Song("In da club", "50 cent", "balimumaikata", "33:21")
#b = Song("Southern Hospitality", "Ludacris", "ddz", "1:12:44")
#c = Song("Hustlin'", "Rick Ross", "pak nz", "1:05")
#d = Song("Get Crunk", "Jim Jones feat. The Game", "nz", "11:05")
#e = Song("asdasd", "asdasdsasa", "asnasdz", "10:00")
#pl = Playlist("Mine", True, True)
#pl.add_songs([a, b, c, d, e])
#pl.pprint_playlist()
#print(pl.total_length())
# pl.artists()
#pl.save()
#pl2 = Playlist.load("Mine.json")
#print(pl.songs)
#print(pl2.songs)

