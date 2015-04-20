import re


class Song:

    def __init__(self, title="Unknown", artist="Unknown", album="Unknown", length="0:00"):
        for x in length.split(":"):
            if int(x) > 59:
                print("Incorrect length of the song !")
                raise ValueError
        else:
            self._title = title
            self._artist = artist
            self._album = album
            self._length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self._artist, self._title, self._album, self._length)

    def __repr__(self):
        return "{}, {}, {}, {}".format(self._title, self._artist, self._album, self._length)

    def __eq__(self, other):
        return self._title == other._title and self._artist == other._artist

    def __hash__(self):
        return hash(self._title + self._artist + self._album)

    def length(self, seconds=False, minutes=False, hours=False):
        total = 0
        lst = self._length.split(":")
        lst = lst[::-1]
        for x in range(0, len(lst)):
            total += int(lst[x]) * 60**x
        if seconds:
            return total
        if minutes:
            return total // 60
        if hours:
            return total // 3600
        else:
            return str(self._length)


#a = Song("dasda", "dasda", "dasd", "43:44:33")
#print(a.length(True, False, False))
