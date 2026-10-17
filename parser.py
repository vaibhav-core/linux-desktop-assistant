
COMMANDS = {
    "volume up": "volume_up",
    "volume down": "volume_down",
    "mute": "mute",
    "lock": "lock",
    "sleep": "sleep",
    "restart": "restart",
    "brightness up": "brightness_up",
    "brightness down": "brightness_down",
}


def parse_command(command):
    command = command.strip()

    if not command:
        return None

    normalized = command.lower()

    if normalized.startswith("open "):
        target = command[5:].strip()
        if target:
            return {"intent": "open", "target": target}

    if normalized.startswith("close "):
        target = command[6:].strip()
        if target:
            return {"intent": "close", "target": target.lower()}

    
    if normalized.startswith("find ") or " in " in normalized:
       
        index=normalized.rfind(" in ")
       
        filename=command[5:index].strip()
        location=command[index+4:].strip()

        if filename and location:
            return {
                "intent":"find file",
                "filename":filename,
                "location":location
            }
    
    if normalized in COMMANDS:
        return {"intent": COMMANDS[normalized], "target": None}

    return None