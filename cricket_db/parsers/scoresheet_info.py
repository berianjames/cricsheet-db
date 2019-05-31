from cricket_db.parsers.parser import Parser


class ScoresheetInfoParser(Parser):
    def __init__(self, match_id):
        self.match_id = match_id

    def parse(self, raw):
        return {
            'match_id': self.match_id,
            'data_version': raw['data_version'],
            'date_created': raw['created'],
            'revision': raw['revision']
        }
