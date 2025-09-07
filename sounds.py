import shutil
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

def list_sounds() -> list:
    sounds = []
    for sound in sorted(os.listdir("sounds")):
        if sound.endswith(('.wav', '.mp3')):
            sounds.append([sound.split('.')[0]])
    return sounds


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
    sounds = list_sounds()
    if not sounds:
        print("No sounds found in the sounds directory")
        return
    
    print("\033[92m\033[1mAvailable sounds:\033[0m")
    for i, sound in enumerate(sounds, 1):
        print(f"{i}. {sound[0]}")
    
    print("\n\033[92m\033[1mEnter the number of the sound to play:\033[0m")
    try:
        choice = int(input().strip())
        if 1 <= choice <= len(sounds):
            play_sound_file(sounds[choice-1][0])
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")

def remove_sound():
    sounds = list_sounds()
    if not sounds:
        print("No sounds found in the sounds directory")
        return
    
    print("\033[92m\033[1mAvailable sounds to remove:\033[0m")
    for i, sound in enumerate(sounds, 1):
        print(f"{i}. {sound[0]}")
    
    print("\n\033[92m\033[1mEnter the number of the sound to remove:\033[0m")
    try:
        choice = int(input().strip())
        if 1 <= choice <= len(sounds):
            sound_name = sounds[choice-1][0]
            sound_files = [f"sounds/{sound_name}.wav", f"sounds/{sound_name}.mp3"]
            for sound_file in sound_files:
                if os.path.exists(sound_file):
                    os.remove(sound_file)
                    print(f"Sound '{sound_name}' removed successfully")
                    return
            print(f"Sound file for '{sound_name}' not found")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")
