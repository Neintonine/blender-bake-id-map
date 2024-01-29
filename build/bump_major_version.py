import os

import versioning

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
CURRENT_VER_FILE = os.path.join(CURRENT_PATH, ".version")


if __name__ == "__main__":
    currentVersion = versioning.get_version()
    nextVersion = currentVersion.bump_major()
    versioning.save_version(nextVersion)
