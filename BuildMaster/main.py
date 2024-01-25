import os
import sc2reader
from enum import Enum

# Specify the directory path
folder_path = "B:/cpp-sc2/BuildMaster/Replays"

# Starcraft 2 username
player_name = "Cstrange"

def race_winrate(player_name):
    """Gather data to determine winrate based on race"""
    replay_counter = 0

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):

            replay_counter +=1
            print(f"Loading replay {replay_counter}.....   ")
            replay = sc2reader.load_replay(file_path, load_map=True)

            # Access basic information
            game_mode = replay.attributes.get(16).get("Game Mode")

            # Players
            player_one = replay.players[0]
            player_two = replay.players[1]

            # Player names
            player_one_name = player_one.name
            player_two_name = player_two.name

            # Player races
            player_one_race = player_one.race 
            player_two_race = player_two.race

            # Game winner name
            if replay.winner:
                for player in replay.players:
                    if player.result == 'Win':
                        winner_name = player.name


"""Determine Build Type"""
class BuildOrder(Enum):
    UNKNOWN = 0
    AGRESSION = 1
    STANDARD = 2
    ECONOMY = 3


command_center_count = 1
production_building_count = 0
build_order = BuildOrder.UNKNOWN

replay = sc2reader.load_replay("B:\cpp-sc2\BuildMaster\Replays\Solaris LE (17).SC2Replay", load_map=True)

# Initialize a dictionary to hold events for each player
player_events = {player: [] for player in replay.players}

# Iterate through events and process only unit events
for event in replay.events:
    if isinstance(event, sc2reader.events.UnitInitEvent):
        player = event.unit.owner
        if player:
            player_events[player].append(event)

for player, events in player_events.items():
    if player.name == "Cstrange":
        print(f"Events for Player {player.name}:")
        for event in events:
            print(f" - {event.unit.name} at {event.second // 60}.{event.second % 60}s")
            if event.unit.name == "OrbitalCommand":
                command_center_count += 1
            elif event.unit.name == "Barracks":
                production_building_count += 1
            elif event.unit.name == "Factory":
                production_building_count += 1
            elif event.unit.name == "Starport":
                production_building_count += 1
            
            if event.second < 300:
                if command_center_count >= 3:
                    build_order = BuildOrder.ECONOMY
                elif production_building_count >= 7:
                    build_order = BuildOrder.AGRESSION
                elif command_center_count == 2 and production_building_count < 7:
                    build_order = BuildOrder.STANDARD
print(command_center_count)
print(production_building_count)
print(build_order.name)