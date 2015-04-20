import unittest
from Panda import Panda


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.panda1 = Panda("Gosho", "gosho@abv.bg", "male")
        self.panda2 = Panda("Gosho", "gosho@abv.bg", 'male')

    def test_isInstance(self):
        self.assertTrue(isinstance(self.panda1, Panda))

    def test_str_func(self):
        self.assertTrue(isinstance(str(self.panda1), str))

    def test_name_func(self):
        self.assertEqual(self.panda1.name(), 'Gosho')

    def test_email_func(self):
        self.assertEqual(self.panda1.email(), "gosho@abv.bg")

    def test_gender_func(self):
        self.assertEqual(self.panda1.gender(), "male")

    def test_isMale_func(self):
        self.assertTrue(self.panda1.isMale())

    def test_isFemale_func(self):
        self.assertFalse(self.panda1.isFemale())

    def test_eq_func(self):
        self.assertEqual(self.panda1, self.panda2)

    def test_hash_func(self):
        self.assertGreater(hash(self.panda1), 111)

    def test_hash_equals(self):
        self.assertEqual(hash(self.panda1), hash(self.panda2))


if __name__ == "__main__":
    unittest.main()
