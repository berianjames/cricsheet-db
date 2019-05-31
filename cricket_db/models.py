from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Team(Base):
    __tablename__ = 'teams'
    name = Column(String, primary_key=True)

    def __repr__(self):
        return "<Team(name='%s')>" % (self.name)


class Competition(Base):
    __tablename__ = 'competitions'
    name = Column(String, primary_key=True)

    def __repr__(self):
        return "<Competition(name='%s')>" % (self.name)


class Player(Base):
    __tablename__ = 'players'
    name = Column(String, primary_key=True)

    def __repr__(self):
        return "<Player(name='%s')>" % (self.name)


class Umpire(Base):
    __tablename__ = 'umpires'
    name = Column(String, primary_key=True)

    def __repr__(self):
        return "<Umpire(name='%s')>" % (self.name)


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    gender = Column(String, nullable=False)
    match_type = Column(String, nullable=False)
    competition = Column(String, ForeignKey('competitions.name'))
    max_overs = Column(Integer)
    venue = Column(String)
    city = Column(String)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)

    team_home = Column(String, ForeignKey('teams.name'), nullable=False)
    team_away = Column(String, ForeignKey('teams.name'), nullable=False)
    result = Column(String, nullable=False)
    method = Column(String)
    winner = Column(String, ForeignKey('teams.name'))
    won_by_type = Column(String)
    won_by_value = Column(Integer)
    player_of_match = Column(String, ForeignKey('players.name'))
    toss_won_by = Column(String, ForeignKey('teams.name'))
    toss_decision = Column(String)
    umpire_first = Column(String, ForeignKey('umpires.name'))
    umpire_second = Column(String, ForeignKey('umpires.name'))
    umpire_third = Column(String, ForeignKey('umpires.name'))
    umpire_forth = Column(String, ForeignKey('umpires.name'))

    team_home_relationship = relationship('Team', foreign_keys=[team_home])
    team_away_relationship = relationship('Team', foreign_keys=[team_away])
    winner_relationship = relationship('Team', foreign_keys=[winner])
    toss_won_by_relationship = relationship('Team', foreign_keys=[toss_won_by])
    player_of_match_relationship = relationship('Player')
    umpire_first_relationship = relationship('Umpire', foreign_keys=[umpire_first])
    umpire_second_relationship = relationship('Umpire', foreign_keys=[umpire_second])
    umpire_third_relationship = relationship('Umpire', foreign_keys=[umpire_third])
    umpire_forth_relationship = relationship('Umpire', foreign_keys=[umpire_forth])

    def __repr__(self):
        return "<Match(id='%s', venue='%s', city='%s', match_type='%s', start_date='%s')>" % (
            self.id, self.venue, self.city, self.match_type, self.start_date)


class Scoresheet(Base):
    __tablename__ = 'scoresheets'

    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    data_version = Column(Numeric(precision=2, scale=1))
    date_created = Column(String)
    revision = Column(Integer)

    match = relationship('Match')

    def __repr__(self):
        return "<Scoresheet(match_id='%s', data_version='%s', created='%s', revision='%s')>" % (
            self.match_id, self.data_version, self.date_created, self.revision)


class Innings(Base):
    __tablename__ = 'innings'

    match_id = Column(Integer, ForeignKey('matches.id'), primary_key=True)
    innings_number = Column(Integer, primary_key=True)
    batting_team = Column(String, ForeignKey('teams.name'), nullable=False)
    penalty_runs_pre = Column(Integer)
    penalty_runs_post = Column(Integer)
    was_declared = Column(Boolean)

    matches = relationship('Match')
    teams = relationship('Team')

    def __repr__(self):
        return "<Innings(id='%s', batting='%s', was_declared='%s')>" % (
            self.id, self.batting_team, self.was_declared)


class Delivery(Base):
    __tablename__ = 'deliveries'

    match_id = Column(Integer, primary_key=True)
    innings_number = Column(Integer, primary_key=True)
    over_number = Column(Integer, primary_key=True)
    ball_number = Column(Integer, primary_key=True)
    batsman_name = Column(String, ForeignKey('players.name'), nullable=False)
    bowler_name = Column(String, ForeignKey('players.name'), nullable=False)
    non_striker_name = Column(String, ForeignKey('players.name'), nullable=False)
    runs_batsman = Column(Integer, nullable=False)
    was_boundary = Column(Boolean, default=0)
    runs_extras = Column(Integer, nullable=False)
    extras_type = Column(String)
    runs_total = Column(Integer, nullable=False)
    has_wicket = Column(Boolean, default=0)

    innings = relationship('Innings', foreign_keys=[match_id, innings_number])
    batsman = relationship('Player', foreign_keys=[batsman_name])
    bowler = relationship('Player', foreign_keys=[bowler_name])
    non_striker = relationship('Player', foreign_keys=[non_striker_name])

    __table_args__ = (
        ForeignKeyConstraint(['match_id', 'innings_number'], ['innings.match_id', 'innings.innings_number']),
    )

    def __repr__(self):
        return "<Delivery(id='%s', batsman='%s', bowler='%s', runs='%s')>" % (
            self.id, self.batsman_name, self.bowler_name, self.runs_total)


class Wicket(Base):
    __tablename__ = 'wickets'

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, nullable=False)
    innings_number = Column(Integer, nullable=False)
    over_number = Column(Integer, nullable=False)
    ball_number = Column(Integer, nullable=False)
    kind = Column(String, nullable=False)
    player_out_name = Column(String, ForeignKey('players.name'), nullable=False)
    fielder_name = Column(String, ForeignKey('players.name'))

    delivery = relationship('Delivery', foreign_keys=[match_id, innings_number, over_number, ball_number])
    player_out = relationship('Player', foreign_keys=[player_out_name])
    fielder = relationship('Player', foreign_keys=[fielder_name])

    __table_args__ = (
        ForeignKeyConstraint(
            ['match_id', 'innings_number', 'over_number', 'ball_number'],
            ['deliveries.match_id', 'deliveries.innings_number', 'deliveries.over_number', 'deliveries.ball_number']
        ),
    )

    def __repr__(self):
        return "<Wicket(player_out='%s', kind='%s')>" % (
            self.batsman_name, self.kind)
