import unittest
from collections import OrderedDict
from cricket_db.parsers.scoresheet_info import ScoresheetInfoParser

MATCH_ID = 947147

fixtures = [
    OrderedDict([('data_version', '0.9'), ('created', '2017-04-30'), ('revision', '1')])
]

output = [
    {'match_id': MATCH_ID, 'data_version': '0.9', 'date_created': '2017-04-30', 'revision': '1'}
]


class TestScoresheetInfoParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.scoresheet_info_parser = ScoresheetInfoParser(self.match_id)

    def test_scoresheet_info_parser(self):
        for fixture, expected in zip(fixtures, output):
            self.assertDictEqual(
                self.scoresheet_info_parser.parse(fixture), expected
            )

if __name__ == '__main__':
    unittest.main()
