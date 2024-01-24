
import os
import sc2reader

# Specify the directory path
folder_path = "C:/Users/codyl/OneDrive/Documents/StarCraft II/Accounts/84959618/1-S2-1-3738305/Replays/Multiplayer"
i = 0
# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if i >= 1:
        break
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        replay = sc2reader.load_replay("C:/Users/codyl/OneDrive/Documents/StarCraft II/Accounts/84959618/1-S2-1-3738305/Replays/Multiplayer/Altitude LE (38).SC2Replay", load_map=True)
        # Access basic information
        print(replay.attributes.get(16).get("Game Mode"))
        print(replay.winner)
        for player in replay.players:
            print(f"Player {player.name} played as {player.play_race}")
    i += 1

# # Loop through events (example)
# for event in replay.events:
#     # Process each event (e.g., unit creation, commands)
#     print(event)


replay = sc2reader.load_replay("C:/Users/codyl/OneDrive/Documents/StarCraft II/Accounts/84959618/1-S2-1-3738305/Replays/Multiplayer/Altitude LE (38).SC2Replay", load_map=True)
"""Winrates Based on Race"""
USERNAME = replay.players[0].name
print("")



"""Determine Build Order"""

"""Winrates Based on Build Order"""