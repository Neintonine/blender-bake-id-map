import os
import shutil

import versioning

ZIP_FILE_NAME = "blender_bake-id-mask_{version}"

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

SOURCE_PATH = os.path.join(CURRENT_PATH, "../src")
TARGET_PATH = os.path.join(CURRENT_PATH, '../dist')

if __name__ == "__main__":

    if not os.path.isdir(TARGET_PATH):
        os.mkdir(TARGET_PATH)

    currentVersion = versioning.get_version()
    nextVersion = currentVersion.bump_build()
    versioning.save_version(nextVersion)

    filename = os.path.join(TARGET_PATH, ZIP_FILE_NAME.format(version=nextVersion.__str__()))
    shutil.make_archive(filename, 'zip', SOURCE_PATH)
