import unittest
from collections import OrderedDict
from cricket_db.parsers.innings import InningsParser

MATCH_ID = 947147
INNINGS_NUMBER = 1

fixtures = [
    OrderedDict([('team', 'Lancashire')]),
    OrderedDict([('team', 'Nottingham'), ('declared', 1)])
]

output = [
    {'match_id': 947147, 'innings_number': 1, 'batting_team': 'Lancashire', 'was_declared': False},
    {'match_id': 947147, 'innings_number': 1, 'batting_team': 'Nottingham', 'was_declared': True}
]


class TestInningsParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.innings_number = INNINGS_NUMBER
        self.innings_parser = InningsParser(self.match_id, self.innings_number)

    def test_innings_parser(self):
        for fixture, expected in zip(fixtures, output):
            self.assertDictEqual(self.innings_parser.parse(fixture), expected)

if __name__ == '__main__':
    unittest.main()
