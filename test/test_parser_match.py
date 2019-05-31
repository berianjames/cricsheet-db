import unittest
from collections import OrderedDict
from cricket_db.parsers.match import MatchParser

MATCH_ID = 947147


class TestMatchParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.match_parser = MatchParser(self.match_id)
        self.fixtures = [
            OrderedDict([
                ('city', 'Nottingham'),
                ('competition', 'NatWest T20 Blast'),
                ('dates', OrderedDict([('date', '2016-06-04')])),
                ('gender', 'male'),
                ('match_type', 'T20'),
                ('outcome', OrderedDict([('by', OrderedDict([('wickets', '2')])), ('winner', 'Nottinghamshire')])),
                ('overs', '20'),
                ('player_of_match', OrderedDict([('player_of_match', 'MH Wessels')])),
                ('teams', OrderedDict([('team', ['Nottinghamshire', 'Lancashire'])])),
                ('toss', OrderedDict([('decision', 'field'), ('winner', 'Nottinghamshire')])),
                ('umpires', OrderedDict([('umpire', ['ID Blackwell', "SJ O'Shaughnessy"])])),
                ('venue', 'Trent Bridge')
            ])
        ]
        self.expected = [{
            'id': 947147,
            'gender': 'male',
            'match_type': 'T20',
            'competition': 'NatWest T20 Blast',
            'max_overs': '20',
            'venue': 'Trent Bridge',
            'city': 'Nottingham',
            'start_date': '2',
            'end_date': '4',
            'team_home': 'Nottinghamshire',
            'team_away': 'Lancashire',
            'player_of_match': 'MH Wessels',
            'toss_won_by': 'Nottinghamshire',
            'toss_decision': 'field',
            'result': 'win',
            'method': None,
            'winner': 'Nottinghamshire',
            'won_by_type': 'wickets',
            'won_by_value': '2',
            'umpire_first': 'ID Blackwell',
            'umpire_second': "SJ O'Shaughnessy",
            'umpire_third': None,
            'umpire_forth': None
        }]

    def test_match_parser(self):
        for fixture, expected in zip(self.fixtures, self.expected):
            self.assertDictEqual(self.match_parser.parse(fixture), expected)

if __name__ == '__main__':
    unittest.main()
