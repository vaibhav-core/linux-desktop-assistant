import subprocess


APPS = {
    "firefox": "firefox",

    "chrome": "google-chrome",
    "browser": "google-chrome",

    "vscode": "code",
    "vs code": "code",
    "code": "code",

    "antigravity": "antigravity",

    "terminal": "ptyxis",
}


def open_app(name):
    name = name.lower().strip()

    if name not in APPS:
        return False

    subprocess.Popen(
        [APPS[name]],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return True


def close_app(name):
    name = name.lower().strip()

    if name not in APPS:
        return False

    # Firefox is installed as a Snap,
    # so its process needs to be closed through its systemd scope.
    if name == "firefox":
        scopes = subprocess.run(
            [
                "systemctl",
                "--user",
                "list-units",
                "--type=scope",
                "--no-legend",
                "--plain",
            ],
            capture_output=True,
            text=True,
        )

        for line in scopes.stdout.splitlines():
            scope = line.split()[0]

            if (
                scope.startswith("snap.firefox.firefox-")
                and scope.endswith(".scope")
            ):
                result = subprocess.run(
                    ["systemctl", "--user", "stop", scope],
                    capture_output=True,
                    text=True,
                )

                return result.returncode == 0

        return False

    # Chrome executable is "google-chrome",
    # but its actual process name is "chrome".
    if name in ("chrome", "browser"):
        result = subprocess.run(
            ["pkill", "-x", "chrome"],
            capture_output=True,
            text=True,
        )

        return result.returncode == 0

    # Other applications
    result = subprocess.run(
        ["pkill", "-x", APPS[name]],
        capture_output=True,
        text=True,
    )

    return result.returncode == 0