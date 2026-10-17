from pathlib import Path

from system.systems import (volume_down,volume_up,restart,sleep,mute,lock,brightness_up,brightness_down)
from parser import parse_command
from system.app import open_app, close_app, APPS
from system.files import open_path,find_file
from parser import COMMANDS


def execute_command(command):
    result = parse_command(command)

    if result is None:
        return False

    intent = result["intent"]
    target = result.get("target")

    # Handle applications
    if intent in ("open", "close") and target in APPS:
        if intent == "open":
            success = open_app(target)
            print(f"{'Opened' if success else 'Error opening'} {target}")
            return success

        if intent == "close":
            success = close_app(target)
            print(f"{'Closed' if success else 'Error closing'} {target}")
            return success

    # Handle system commands
    system_commands = {
        "volume_up": volume_up,
        "volume_down": volume_down,
        "mute": mute,
        "sleep": sleep,
        "restart": restart,
        "lock": lock,
        "brightness_up": brightness_up,
        "brightness_down": brightness_down,
    }

    if intent in system_commands:
        return system_commands[intent]()

    # Handle filesystem paths

    if intent=="open":
        return open_path(target)

    if intent=="find file":
        
        location=result["location"]
        location=Path(location).expanduser()
        
        filename=result["filename"]
        
        if not location.is_absolute():
            location=Path.home() / location
        
        found=find_file(filename,location)
        
        if len(found)==0:
            print("NO MATCHES FOUND")
            return False

        elif len(found)==1:
            print(f"found 1 result opening")
            return open_path(found[0])


        else:
            
            print(f"found {len(found)} results")
            
            for i,x in enumerate(found,start=1):
                print(f"{i}. {x}")
            
            try:
                choice=int(input("Select a path to open\n"))
                if 1<=choice<=len(found):
                    return open_path(found[choice-1])
            except ValueError:
                print("Please enter a valid number")
                return False            
    return False
