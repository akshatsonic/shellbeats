import argparse
from sounds import add_sound, list_sounds, play_sound, remove_sound
from configure import add_configuration, list_configurations, remove_configuration
import exception_handler
import sys

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