def play_sound_on_cli(command):
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
    
    if len(command.split()) > 2:
        words = command.split()[:2]
        if " ".join(words) in config:
            play_sound_file(config[" ".join(words)])
        elif words[0] in config:
            play_sound_file(config[words[0]])
    elif command in config:
        play_sound_file(config[command])