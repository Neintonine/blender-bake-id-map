import os
import shutil
import zipfile

import versioning

ZIP_FILE_NAME = "blender_bake-id-mask_{version}.zip"
PROJECT_NAME = "Bake ID Mask"

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
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zip:
        for (root, dirs, files) in os.walk(SOURCE_PATH):
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')

            for file in files:

                relativePath = os.path.relpath(
                    os.path.join(root, file),
                    SOURCE_PATH
                )

                zip.write(
                    os.path.join(root, file),
                    os.path.join(PROJECT_NAME, relativePath)
                )