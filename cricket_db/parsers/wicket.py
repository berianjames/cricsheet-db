from cricket_db.parsers.parser import Parser


class WicketParser(Parser):
    def __init__(self, match_id, innings_number, over_number, ball_number):
        self.match_id = match_id
        self.innings_number = innings_number
        self.over_number = over_number
        self.ball_number = ball_number

    def parse(self, raw):
        wicket = {
            'match_id': self.match_id,
            'innings_number': self.innings_number,
            'over_number': self.over_number,
            'ball_number': self.ball_number,
            'kind': raw['kind'],
            'player_out_name': raw['player_out'],
        }
        if 'fielders' in raw:
            ensure_list = lambda x: [x] if not isinstance(x, list) else x
            wicket.update({'fielder_name': ensure_list(raw['fielders']['fielder'])[0]})
        return wicket
