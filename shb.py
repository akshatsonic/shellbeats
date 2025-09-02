import argparse
from sounds import add_sound, list_sounds, play_sound, remove_sound
from configure import add_configuration, list_configurations, remove_configuration
import exception_handler
import sys

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

def main():
    parser = argparse.ArgumentParser(description="Shellbeats CLI Tool")
    command_subparsers = parser.add_subparsers(dest='command',help='Command to run', required=True)
    
    sounds_parser = command_subparsers.add_parser('sounds', help='Command to run')
    sounds_parser.add_argument('-l','--list', action='store_true', help='List all sounds')
    sounds_parser.add_argument('-p','--play', action='store_true', help='Play a sound')
    sounds_parser.add_argument('-a','--add', action='store_true', help='Add a new sound')
    sounds_parser.add_argument('-r','--remove', action='store_true', help='Remove a sound')

    config_parser = command_subparsers.add_parser('configure', help='Command to run')
    config_parser.add_argument('-a','--add', action='store_true', help='Add a new configuration for a cli command')
    config_parser.add_argument('-l','--list', action='store_true', help='List all configurations')
    config_parser.add_argument('-r','--remove', action='store_true', help='Remove a configuration')
    
    
    args = parser.parse_args()
    if args.command == 'sounds':
        if args.list:
            list_sounds()
        elif args.play:
            play_sound()
        elif args.add:
            add_sound()
        elif args.remove:
            remove_sound()
    elif args.command == 'configure':
        if args.add:
            add_configuration()
        elif args.list:
            list_configurations()
        elif args.remove:
            remove_configuration()
    else:
        parser.print_help()

if __name__ == '__main__':
    sys.excepthook = exception_handler.my_exception_handler
    main() 