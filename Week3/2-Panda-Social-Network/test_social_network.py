import unittest
from Panda import Panda
from SocialNetwork import SocialNetwork
from custom_exceptions import PandaAlreadyThere
from custom_exceptions import PandasAlreadyThere


class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.sn1 = SocialNetwork()
        self.panda1 = Panda("Gosho", "haha@abv.bg", "male")
        self.panda2 = Panda("Pesho", "pesho@abv.bg", "female")
        self.panda3 = Panda("Sasho", "sasho@abv.bg", "female")
        self.panda4 = Panda("Spas", "ada@asd.bg", "male")

    def test_socialnetwork_var(self):
        self.assertTrue(isinstance(self.sn1, SocialNetwork))

    def test_socialnetwork_database(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        self.sn1.make_friends(self.panda2, self.panda3)
        self.sn1.make_friends(self.panda2, self.panda4)
        self.sn1.make_friends(self.panda3, self.panda4)
        self.assertEqual(len(self.sn1.database), 4)

    def test_add_panda_func(self):
        self.sn1.add_panda(self.panda1)
        self.assertEqual(len(self.sn1.database), 1)

    def test_has_panda_func(self):
        self.sn1.add_panda(self.panda1)
        self.assertTrue(self.sn1.has_panda(self.panda1))

    def test_make_friends_func(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        self.assertEqual(len(self.sn1.database), 2)
        self.assertGreater(len(self.sn1.database[self.panda1]), 0)
        self.assertGreater(len(self.sn1.database[self.panda1]), 0)
        self.assertTrue(self.panda2 in self.sn1.database[self.panda1])
        self.assertTrue(self.panda1 in self.sn1.database[self.panda2])

    def test_PandAlreadyThere_exc(self):
        self.sn1.add_panda(self.panda1)
        with self.assertRaises(PandaAlreadyThere):
            self.sn1.add_panda(self.panda1)

    def test_PandasAlreadyThere_exc(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        with self.assertRaises(PandasAlreadyThere):
            self.sn1.make_friends(self.panda1, self.panda2)

    def test_are_frineds_func(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        self.assertTrue(self.sn1.are_friends(self.panda1, self.panda2))

    def test_friends_of_func(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        self.assertGreater(len(self.sn1.friends_of(self.panda2)), 0)

    def test_friends_of_not_in_the_network(self):
        # self.sn1.add_panda(self.panda2)
        self.assertIsInstance(self.sn1.friends_of(self.panda2), bool)

    def test_connection_level_func(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        self.sn1.make_friends(self.panda2, self.panda3)
        self.sn1.make_friends(self.panda2, self.panda4)
        self.sn1.make_friends(self.panda3, self.panda4)
        self.assertEqual(self.sn1.connection_level(self.panda1, self.panda2), 1)

    def test_are_conected_func(self):
        self.sn1.make_friends(self.panda1, self.panda2)
        #self.assertEqual(self.sn1.connection_level(self.panda1, self.panda2), 1)
        self.assertTrue(self.sn1.are_connected(self.panda1, self.panda2))
        self.sn1.add_panda(self.panda3)
        self.assertFalse(self.sn1.are_connected(self.panda3, self.panda4))


if __name__ == "__main__":
    unittest.main()
