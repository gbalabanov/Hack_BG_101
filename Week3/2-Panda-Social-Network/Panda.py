import re
import json


class Panda():

    def __init__(self, _name, _email, _gender):
        match = re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", _email)
        if match:
            self._email = _email
        else:
            print("Not a valid email!")
            raise ValueError
        _gender = _gender.lower()
        if _gender != "male" and _gender != "female":
            print("Enter correct gender !")
            raise ValueError
        self._name = _name
        self._gender = _gender
        self._friendsList = []

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        self._gender = self._gender.lower()
        return self._gender == 'male'

    def isFemale(self):
        self._gender = self._gender.lower()
        return self._gender == 'female'

    def serialize(self):
        return json.dumps(repr(self), indent=4)

    def __str__(self):
        return "{} - {} - {}".format(self._name, self._email, self._gender)

    def __eq__(self, other):
        equal_names = self.name() == other.name()
        equal_emails = self.email() == other.email()
        equal_genders = self.gender() == other.gender()
        return equal_emails and equal_genders and equal_names

    def __repr__(self):
        return "Panda({}, {}, {})".format(self._name, self._email, self._gender)

    def __hash__(self):
        return hash(self.name()) + hash(self.email()) + hash(self.gender())
