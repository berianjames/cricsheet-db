import unittest
from cricket_db.parsers.delivery import DeliveryParser

MATCH_ID = 947147
INNINGS_NUMBER = 1
OVER_NUMBER = 4
BALL_NUMBER = 2

fixtures = [
    {
        'batsman': 'MJ Guptill',
        'bowler': 'LJ Fletcher',
        'non_striker': 'AN Petersen',
        'runs': {'batsman': 0, 'extras': 0, 'total': 0}
    },
    {
        'batsman': 'MJ Guptill',
        'bowler': 'LJ Fletcher',
        'non_striker': 'AN Petersen',
        'runs': {'batsman': 0, 'extras': 0, 'total': 0},
        'wickets': {}
    }
]

output = [
    {
        'match_id': 947147,
        'innings_number': 1,
        'over_number': 4,
        'ball_number': 2,
        'batsman_name': 'MJ Guptill',
        'bowler_name': 'LJ Fletcher',
        'non_striker_name': 'AN Petersen',
        'has_wicket': False,
        'runs_batsman': 0,
        'was_boundary': False,
        'runs_extras': 0,
        'runs_total': 0
    },
    {
        'match_id': 947147,
        'innings_number': 1,
        'over_number': 4,
        'ball_number': 2,
        'batsman_name': 'MJ Guptill',
        'bowler_name': 'LJ Fletcher',
        'non_striker_name': 'AN Petersen',
        'has_wicket': True,
        'runs_batsman': 0,
        'was_boundary': False,
        'runs_extras': 0,
        'runs_total': 0
    }
]


class TestDeliveryParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.innings_number = INNINGS_NUMBER
        self.over_number = OVER_NUMBER
        self.ball_number = BALL_NUMBER
        self.delivery_parser = DeliveryParser(
            self.match_id,
            self.innings_number,
            self.over_number,
            self.ball_number
        )

    def test_delivery_parser(self):
        for fixture, expected in zip(fixtures, output):
            self.assertDictEqual(
                self.delivery_parser.parse(fixture), expected
            )

if __name__ == '__main__':
    unittest.main()
