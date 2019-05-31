import unittest
from collections import OrderedDict
from cricket_db.parsers.wicket import WicketParser

MATCH_ID = 947147
INNINGS_NUMBER = 1
OVER_NUMBER = 4
BALL_NUMBER = 2

fixtures = [
    {'kind': 'lbw', 'player_out': 'SK Warne'},
    {'kind': 'caught', 'player_out': 'SK Warne', 'fielders': {'fielder': 'SR Watson'}}
]

output = [
    {'match_id': 947147, 'innings_number': 1, 'over_number': 4, 'ball_number': 2, 'kind': 'lbw', 'player_out_name': 'SK Warne'},
    {'match_id': 947147, 'innings_number': 1, 'over_number': 4, 'ball_number': 2, 'kind': 'caught', 'player_out_name': 'SK Warne', 'fielder_name': 'SR Watson'}
]


class TestWicketParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.innings_number = INNINGS_NUMBER
        self.over_number = OVER_NUMBER
        self.ball_number = BALL_NUMBER
        self.wicket_parser = WicketParser(
            self.match_id,
            self.innings_number,
            self.over_number,
            self.ball_number
        )

    def test_wicket_parser(self):
        for fixture, expected in zip(fixtures, output):
            self.assertDictEqual(
                self.wicket_parser.parse(fixture), expected
            )

if __name__ == '__main__':
    unittest.main()
