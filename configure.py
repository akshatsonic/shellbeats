from sounds import list_sounds
import json
import os
from terminaltables import SingleTable

def add_configuration():
    print("Enter the command to configure:")
    command = input()
    #validate cli command should not have more than 2 words
    if len(command.split()) > 2:
        raise ValueError("Command should not have more than 2 words")
    sounds = list_sounds()
    print("Enter the serial number of sound to play:")
    sound = input()
    if int(sound) < 1 or int(sound) > len(sounds):
        raise ValueError("Invalid serial number")
    sound_name = sounds[int(sound)][1]
    config = {}
    # Try to read existing config if file exists and is not empty
    if os.path.exists("config.json") and os.path.getsize("config.json") > 0:
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print("Warning: config.json is corrupted. Creating a new configuration.")
            config = {}
    
    # Update configuration
    config[command] = sound_name
    
    # Write back to file
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    print(f"✅ Configured '{command}' to play sound: {sound_name}")


def list_configurations():
    if os.path.exists("config.json") and os.path.getsize("config.json") > 0:
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print("Warning: config.json is corrupted. Creating a new configuration.")
            config = {}
    else:
        config = {}
    
    if not config:
        print("No configurations found")
        return
    
    table_data = [["Command", "Sound Name"]]
    for command, sound_name in config.items():
        table_data.append([command, sound_name])
    table = SingleTable(table_data)
    table.inner_column_border = True
    table.justify_columns = {0: "center", 1: "left"}
    table.inner_heading_row_border = True
    print(table.table)
    
def remove_configuration():
    if os.path.exists("config.json") and os.path.getsize("config.json") > 0:
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            print("Warning: config.json is corrupted. Creating a new configuration.")
            config = {}
    else:
        config = {}
    
    if not config:
        print("No configurations found")
        return
    
    print("Enter the command to remove configuration:")
    command = input()
    if command not in config:
        print(f"Configuration for '{command}' not found")
        return
    del config[command]
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    print(f"✅ Removed configuration for '{command}'")