import os
import xmltodict
from cricket_db.models import Scoresheet, Match, Team, Competition
from cricket_db.models import Player, Umpire, Innings, Delivery, Wicket
from cricket_db.parsers.scoresheet_info import ScoresheetInfoParser
from cricket_db.parsers.match import MatchParser
from cricket_db.parsers.innings import InningsParser
from cricket_db.parsers.delivery import DeliveryParser
from cricket_db.parsers.wicket import WicketParser

ENSURE_LIST = lambda x: [x] if not isinstance(x, list) else x


class CricsheetXMLReader(object):
    def __init__(self):
        pass

    def get_objects_from_directory(self, directory):
        objects = list()
        for index in os.listdir(directory):
            for filename in os.listdir('/'.join([directory, index])):
                match_id = filename.split('.')[0]
                with open('/'.join([directory, index, filename]), 'r') as stream:
                    raw = xmltodict.parse(stream.read())['cricsheet']

                scoresheet_info_parser = ScoresheetInfoParser(match_id)
                objects.append(Scoresheet(**scoresheet_info_parser.parse(raw['meta'])))
                match_parser = MatchParser(match_id)
                objects.append(Match(**match_parser.parse(raw['info'])))

                for innings in ENSURE_LIST(raw['innings']['inning']):
                    innings_number = innings['inningsNumber']
                    innings_parser = InningsParser(match_id, innings_number)
                    objects.append(Innings(**innings_parser.parse(innings)))

                    for delivery in ENSURE_LIST(innings['deliveries']['delivery']):
                        over_number, ball_number = delivery['over'], delivery['ball']
                        delivery_parser = DeliveryParser(match_id, innings_number, over_number, ball_number)
                        objects.append(Delivery(**delivery_parser.parse(delivery)))

                        if 'wickets' in delivery:
                            for wicket in ENSURE_LIST(delivery['wickets']['wicket']):
                                wicket_parser = WicketParser(match_id, innings_number, over_number, ball_number)
                                objects.append(Wicket(**wicket_parser.parse(wicket)))
        return objects
