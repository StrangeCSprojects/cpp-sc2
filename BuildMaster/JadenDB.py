from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import sc2reader

Base = declarative_base()

class Map(Base):
    __tablename__ = 'maps'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    race = Column(String)

    map_id = Column(Integer, ForeignKey('maps.id'))
    map = relationship('Map', back_populates='players')

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    mode = Column(String)
    winner = Column(String)

    map_id = Column(Integer, ForeignKey('maps.id'))
    map = relationship('Map', back_populates='games')

Map.players = relationship('Player', back_populates='map')
Map.games = relationship('Game', back_populates='map')

# Create an SQLite database engine
engine = create_engine('sqlite:///starcraft.db')

# Create tables
Base.metadata.create_all(engine)

def insert_game_data(replay_file):
    # Load the replay file
    replay = sc2reader.load_replay(replay_file)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert data into the 'maps' table
    map_data = Map(name=replay.map_name)
    session.add(map_data)
    session.commit()

    # Insert data into the 'players' table
    for player in replay.players:
        player_data = Player(name=player.name, race=player.play_race, map=map_data)
        session.add(player_data)

    # Determine the winner and insert data into the 'games' table
    winner = max(replay.teams, key=lambda team: team.result).players[0].name
    game_data = Game(mode=replay.real_type, winner=winner, map=map_data)
    session.add(game_data)

    # Commit changes
    session.commit()

# Replace 'example.SC2Replay' with the path to your replay file
insert_game_data("example.SC2Replay")
