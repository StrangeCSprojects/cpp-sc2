import os
import sc2reader
from enum import Enum

# Build order types
class BuildOrder(Enum):
    UNKNOWN = 0
    AGRESSION = 1
    STANDARD = 2
    ECONOMY = 3

def replay_analysis(player_name, folder_path):
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
            player_one_race = player_one.play_race 
            player_two_race = player_two.play_race

            # Game winner name
            if replay.winner:
                for player in replay.players:
                    if player.result == 'Win':
                        winner_name = player.name

            # Determine build order            
            print(f"Player Name: {player_name}\nGame Mode: {game_mode}\nPlayer One: {player_one_name} - {player_one_race}\nPlayer Two: {player_two_name} - {player_two_race}\nWinner: {winner_name}")
            build_order(replay)
            print("\n")

def build_order(replay):
    """Determine build order"""
    command_center_count = 1
    production_building_count = 0
    build_order = BuildOrder.UNKNOWN

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

                game_speed_factor = 1.4
                real_time_seconds = int(event.second / game_speed_factor)
                # print(f" - {event.unit.name} at {int(real_time_seconds // 60)}.{real_time_seconds % 60}s")
                if event.unit.name == "OrbitalCommand" or event.unit.name == "OrbitalCommandFlying" :
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
    # print(command_center_count)
    # print(production_building_count)
    print(f"Build Order: {build_order.name}")


def main():
    # Specify the directory path
    folder_path = "C:/cpp-sc2/BuildMaster/Replays" # REMEBER TO UPDATE!!!

    # Starcraft 2 username
    player_name = "Cstrange"
    
    replay_analysis(player_name,folder_path)
if __name__ == "__main__":
    main()