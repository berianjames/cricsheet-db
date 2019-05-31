import unittest
from collections import OrderedDict
from cricket_db.parsers.match import UmpireParser

MATCH_ID = 947147


class TestMatchUmpireParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.match_umpire_parser = UmpireParser()
        self.fixtures = [
            ['ID Blackwell', "SJ O'Shaughnessy"],
            ['ID Blackwell', "SJ O'Shaughnessy", 'P Reiffel']
        ]
        self.expected = [
            {
                'umpire_first': 'ID Blackwell',
                'umpire_second': "SJ O'Shaughnessy",
                'umpire_third': None,
                'umpire_forth': None
            },
            {
                'umpire_first': 'ID Blackwell',
                'umpire_second': "SJ O'Shaughnessy",
                'umpire_third': 'P Reiffel',
                'umpire_forth': None
            }
        ]

    def test_match_umpire_parser(self):
        for fixture, expected in zip(self.fixtures, self.expected):
            self.assertDictEqual(self.match_umpire_parser.parse(fixture), expected)

if __name__ == '__main__':
    unittest.main()
