import unittest
from Song import Song
from Playlist import Playlist


class TestPlayList(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("a", "b", "ab", "2:00")
        self.song2 = Song("aa", "b", "ab", "3:00")
        self.song3 = Song("aa", "bb", "aabb", "2:00")
        self.pl = Playlist("Mine")

    def test_equal_song(self):
        self.assertNotEqual(self.song1, self.song2)

    def test_add_song(self):
        self.pl.add_song(self.song1)
        self.assertEqual(len(self.pl.songs), 1)
        #self.assertEqual(self.pl.add_song(self.song2), "Fail !")
        self.assertEqual(self.song1._length,self.song3._length)
4
    def test_add_songs(self):
        self.assertEqual(self.pl.add_songs(3), "Check your list !")
        lst = [self.song1, self.song2, self.song3, 3]
        self.pl.add_songs(lst)
        self.assertEqual(len(self.pl.songs), 3)

    def test_total_length(self):
        self.pl.add_songs([self.song1, self.song2, self.song3])
        self.assertEqual(self.pl.total_length(), "00:07:00")


if __name__ == '__main__':
    unittest.main()
