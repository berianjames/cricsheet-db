import unittest
from collections import OrderedDict
from cricket_db.parsers.match import MatchOutcomeParser

MATCH_ID = 947147


class TestMatchOutcomeParser(unittest.TestCase):
    def setUp(self):
        self.match_id = MATCH_ID
        self.match_outcome_parser = MatchOutcomeParser()
        self.fixtures = fixtures = [
            {'by': {'runs': 38}, 'winner': 'Pune Warriors'},
            {'by': {'wickets': 7}, 'method': 'D/L', 'winner': 'Sri Lanka'},
            {'by': {'runs': 110}, 'method': 'D/L', 'winner': 'England'},
            {'result': 'tie', 'eliminator': 'Lahore Qalandars'},
            {'method': 'D/L', 'result': 'tie'},
            {'result': 'draw'},
            {'result': 'no result'},
            {'by': {'innings': 1, 'runs': 129}, 'winner': 'South Africa'}
        ]
        self.expected = [
            {'result': 'win', 'method': None, 'winner': 'Pune Warriors', 'won_by_type': 'runs', 'won_by_value': 38},
            {'result': 'win', 'method': 'D/L', 'winner': 'Sri Lanka', 'won_by_type': 'wickets', 'won_by_value': 7},
            {'result': 'win', 'method': 'D/L', 'winner': 'England', 'won_by_type': 'runs', 'won_by_value': 110},
            {'result': 'win', 'method': 'eliminator', 'winner': 'Lahore Qalandars', 'won_by_type': None, 'won_by_value': None},
            {'result': 'tie', 'method': 'D/L', 'winner': None, 'won_by_type': None, 'won_by_value': None},
            {'result': 'draw', 'method': None, 'winner': None, 'won_by_type': None, 'won_by_value': None},
            {'result': 'no result', 'method': None, 'winner': None, 'won_by_type': None, 'won_by_value': None},
            {'result': 'win', 'method': None, 'winner': 'South Africa', 'won_by_type': 'innings_and_runs', 'won_by_value': 129}
        ]

    def test_match_outcome_parser(self):
        for fixture, expected in zip(self.fixtures, self.expected):
            self.assertDictEqual(self.match_outcome_parser.parse(fixture), expected)

if __name__ == '__main__':
    unittest.main()
