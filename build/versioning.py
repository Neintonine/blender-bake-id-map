import os

import semver

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
CURRENT_VER_FILE = os.path.join(CURRENT_PATH, ".version")


def get_version():
    if not os.path.isfile(CURRENT_VER_FILE):
        return semver.Version.parse('1.0.0')
    with open(CURRENT_VER_FILE) as f:
        content = f.read()
        return semver.Version.parse(content)


def save_version(version: semver.Version):
    with open(CURRENT_VER_FILE, 'w') as f:
        f.write(version.__str__())
