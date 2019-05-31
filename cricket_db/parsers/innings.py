from cricket_db.parsers.parser import Parser


class InningsParser(Parser):
    def __init__(self, match_id, innings_number):
        self.match_id = match_id
        self.innings_number = innings_number

    def parse(self, raw):
        innings = {
            'match_id': self.match_id,
            'innings_number': self.innings_number,
            'batting_team': raw['team'],
            'was_declared': ('declared' in raw)
        }
        if 'penalty_runs' in raw:
            innings.update(self.__penalty_runs_parser(raw['penalty_runs']))
        return innings

    def __penalty_runs_parser(self, penalty_runs):
        return {
            'penalty_runs_pre': penalty_runs['pre'] if 'pre' in penalty_runs else None,
            'penalty_runs_post': penalty_runs['post'] if 'post' in penalty_runs else None
        }
