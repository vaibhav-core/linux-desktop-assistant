import subprocess
import shutil
from pathlib import Path

def open_path(path):
    path=Path(path).expanduser()

    if not path.exists():
        return False

    subprocess.Popen(["xdg-open",str(path)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

    return True

def find_file(filename,directory="~"):
    directory=Path(directory).expanduser()

    if not directory.is_dir():
        return []

    results=[]

    for path in directory.rglob(filename):
        if path.is_file():
            results.append(path)
    
    return results

def create_folder(path):
    path=Path(path).expanduser

    path.mkdir(parents=True,exist_ok=True)

    return True

def copy_files(source, destination):
    source=Path(source).expanduser
    destination=Path(destination).expanduser

    if not source.exists():
        return False
    shutil.copy2(source,destination)

    return True

def move_files(src,dest):
    src=Path(src).expanduser
    dest=Path(dest).expanduser

    if not src.exists():
        return False
    shutil.move(src,dest)

    return True