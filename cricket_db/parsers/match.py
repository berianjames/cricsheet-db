from cricket_db.parsers.parser import Parser


class MatchParser(Parser):
    def __init__(self, match_id):
        self.match_id = match_id
        self.metadata_parser = MatchMetadataParser()
        self.outcome_parser = MatchOutcomeParser()
        self.umpire_parser = UmpireParser()

    def parse(self, raw):
        data = {'id': self.match_id}
        data.update(self.metadata_parser.parse(raw))
        data.update(self.outcome_parser.parse(raw['outcome']))
        if 'umpires' in raw:
            data.update(self.umpire_parser.parse(raw['umpires']['umpire']))
        return data


class MatchMetadataParser(Parser):
    def __init__(self):
        pass

    def parse(self, metadata):
        if 'player_of_match' in metadata:
            if type(metadata['player_of_match']['player_of_match']) == list:
                player_of_match = metadata['player_of_match']['player_of_match'][0]
            else:
                player_of_match = metadata['player_of_match']['player_of_match']
        else:
            player_of_match = None
        return {
            'gender': metadata['gender'],
            'match_type': metadata['match_type'],
            'competition': metadata['competition'] if 'competition' in metadata else None,
            'max_overs': metadata['overs'] if 'overs' in metadata else None,
            'venue': metadata['venue'] if 'venue' in metadata else None,
            'city': metadata['city'] if 'city' in metadata else None,
            'start_date': metadata['dates']['date'][0],
            'end_date': metadata['dates']['date'][-1],
            'team_home': metadata['teams']['team'][0],
            'team_away': metadata['teams']['team'][1],
            'player_of_match': player_of_match,
            'toss_won_by': metadata['toss']['winner'],
            'toss_decision': metadata['toss']['decision']
        }


class MatchOutcomeParser(Parser):
    def __init__(self):
        pass

    def parse(self, outcome):
        has_winner = (any(result in outcome for result in ('winner', 'eliminator')))
        result = 'win' if has_winner else outcome['result']

        method = 'D/L' if 'method' in outcome else \
            'eliminator' if 'eliminator' in outcome else None
        winner = outcome['winner'] if 'winner' in outcome else \
            outcome['eliminator'] if 'eliminator' in outcome else None

        by = outcome['by'] if 'by' in outcome else None
        if (not has_winner) or ('eliminator' in outcome):
            won_by_type = None
            won_by_value = None
        elif ('innings' in by) and ('wickets' in by):
            won_by_type = 'innings_and_wickets'
            won_by_value = by['wickets']
        elif ('innings' not in by) and ('wickets' in by):
            won_by_type = 'wickets'
            won_by_value = by['wickets']
        elif ('innings' in by) and ('runs' in by):
            won_by_type = 'innings_and_runs'
            won_by_value = by['runs']
        elif ('innings' not in by) and ('runs' in by):
            won_by_type = 'runs'
            won_by_value = by['runs']

        return {
            'result': result,
            'method': method,
            'winner': winner,
            'won_by_type': won_by_type,
            'won_by_value': won_by_value
        }


class UmpireParser(Parser):
    def __init__(self):
        pass

    def parse(self, umpires):
        if len(umpires) == 2:
            first, second = umpires
            third, forth = None, None
        if len(umpires) == 3:
            first, second, third = umpires
            forth = None
        if len(umpires) == 4:
            first, second, third, forth = umpires
        return {
            'umpire_first': first,
            'umpire_second': second,
            'umpire_third': third,
            'umpire_forth': forth
        }
