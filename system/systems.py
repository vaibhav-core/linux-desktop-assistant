import subprocess

def volume_up():
    
    result=subprocess.run(["amixer","sset","Master","5%+"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    
    return result.returncode == 0

def volume_down():
    
    result=subprocess.run(["amixer","sset","Master","5%-"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)

    return result.returncode == 0

def mute():
    
    result=subprocess.run(["amixer","sset","Master","toggle"],
                          stderr=subprocess.DEVNULL,
                          stdout=subprocess.DEVNULL)

    return result.returncode == 0

def lock():
    result=subprocess.run(["loginctl","lock-session"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)

    return result.returncode==0

def sleep():
    result=subprocess.run(["systemctl","suspend"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)

    return result.returncode==0

def restart():
    result=subprocess.run(["systemctl","reboot"],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)

    return result.returncode==0

def brightness_up():
    result = subprocess.run(["brightnessctl", "set","5%+"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)

    return result.returncode==0

def brightness_down():
    result = subprocess.run(["brightnessctl", "set","5%-"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)

    return result.returncode==0