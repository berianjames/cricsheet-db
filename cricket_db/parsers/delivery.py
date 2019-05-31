from cricket_db.parsers.parser import Parser


class DeliveryParser(Parser):
    def __init__(self, match_id, innings_number, over_number, ball_number):
        self.match_id = match_id
        self.innings_number = innings_number
        self.over_number = over_number
        self.ball_number = ball_number

    def parse(self, raw):
        delivery = {
            'match_id': self.match_id,
            'innings_number': self.innings_number,
            'over_number': self.over_number,
            'ball_number': self.ball_number,
            'batsman_name': raw['batsman'],
            'bowler_name': raw['bowler'],
            'non_striker_name': raw['non_striker'],
            'has_wicket': ('wickets' in raw)
        }
        if 'runs' in raw:
            delivery.update(self.__runs_parser(raw['runs']))
        if 'extras' in raw:
            delivery.update(self.__extras_parser(raw['extras']))
        return delivery

    def __runs_parser(self, runs):
        return {
            'runs_batsman': runs['batsman'],
            'was_boundary': ('non_boundary' not in runs) and (runs['batsman'] == 4 or runs['batsman'] == 6),
            'runs_extras': runs['extras'],
            'runs_total': runs['total']
        }

    def __extras_parser(self, extras):
        return {
            'extras_type': next(iter(extras))
        }
