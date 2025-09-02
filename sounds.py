import shutil
from terminaltables import SingleTable
import os
import subprocess
import threading

def add_sound():
    print("Name of the sound:")
    name = input()
    # name validation
    if not name.isalnum():
        raise ValueError("Name must contain only alphanumeric characters")
    print("Path to the sound file:")
    path = input()
    # path validation to check .wav or .mp3
    if not shutil.os.path.exists(path):
        raise ValueError("Path does not exist")
    if not path.endswith(".wav") and not path.endswith(".mp3"):
        raise ValueError("File must be a .wav or .mp3 file")
    if shutil.os.path.exists(f"sounds/{name}.wav") or shutil.os.path.exists(f"sounds/{name}.mp3"):
        raise ValueError("Sound with this name already exists")
    shutil.copyfile(src=path, dst=f"sounds/{name}.{path.split('.')[-1]}")
    print("Sound added successfully")

def list_sounds() -> map:
    sound_count = len(shutil.os.listdir("sounds"))
    table_data = [["No.", "Sound Name"]]
    for cnt, sound in enumerate(shutil.os.listdir("sounds"), start=1):
        table_data.append([str(cnt).zfill(len(str(sound_count))), sound.split('.')[0]])
    print(f"\033[92m\033[1mAvailable Sounds: {sound_count}\033[0m")
    table = SingleTable(table_data)
    table.inner_column_border = True
    table.justify_columns = {0: "center", 1: "left"}
    table.inner_heading_row_border = True
    print(table.table)
    return table_data


def play_sound_file(sound_name):
    if not shutil.os.path.exists(f"sounds/{sound_name}.wav") and not shutil.os.path.exists(f"sounds/{sound_name}.mp3"):
        raise ValueError(f"Sound '{sound_name}' not found in sounds directory")
    
    thread = threading.Thread(target=play_sound_file_thread, args=(sound_name,))
    thread.start()

def play_sound_file_thread(sound_name):
    if shutil.os.path.exists(f"sounds/{sound_name}.wav"):
        subprocess.run(["afplay", f"sounds/{sound_name}.wav"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(["afplay", f"sounds/{sound_name}.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def play_sound():
    table_data = list_sounds()

    print("\033[92m\033[1mEnter the serial number of the sound to play:\033[0m")
    try:
        serial_number = int(input())
        if serial_number < 1 or serial_number >= len(table_data):
            raise ValueError("Invalid serial number")
        sound_name = table_data[serial_number][1]  # Get the sound name from the table
        play_sound_file(sound_name)
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            raise ValueError("Please enter a valid number") from e
        raise ValueError("Invalid serial number")

def remove_sound():
    table_data = list_sounds()
    print("\033[92m\033[1mEnter the serial number of the sound to remove:\033[0m")
    try:
        serial_number = int(input())
        if serial_number < 1 or serial_number >= len(table_data):
            raise ValueError("Invalid serial number")
        sound_name = table_data[serial_number][1]  # Get the sound name from the table
        sound_files = [f"sounds/{sound_name}.wav", f"sounds/{sound_name}.mp3"]
        for sound_file in sound_files:
            if os.path.exists(sound_file):
                os.remove(sound_file)
                break
        print(f"Sound '{sound_name}' removed successfully")
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            raise ValueError("Please enter a valid number") from e
        raise ValueError("Invalid serial number")
