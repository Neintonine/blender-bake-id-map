import os
import shutil
import zipfile

import versioning

ZIP_FILE_NAME = "blender_bake-id-mask_{version}.zip"
PROJECT_NAME = "Bake ID Mask"

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

SOURCE_PATH = os.path.join(CURRENT_PATH, "../src")
INIT_FILE_PATH = os.path.join(SOURCE_PATH, "__init__.py")
TARGET_PATH = os.path.join(CURRENT_PATH, '../dist')

if __name__ == "__main__":

    if not os.path.isdir(TARGET_PATH):
        os.mkdir(TARGET_PATH)

    currentVersion = versioning.get_version()
    nextVersion = currentVersion.bump_build()
    versioning.save_version(nextVersion)

    filename = os.path.join(TARGET_PATH, ZIP_FILE_NAME.format(version=nextVersion.__str__()))
    original_init_content = ''
    with open(INIT_FILE_PATH, 'r') as f:
        original_init_content = f.read()

    version_insert = original_init_content.replace('# !VERSION', '"version": ({}, {}, {}),'.format(nextVersion.major, nextVersion.minor, nextVersion.patch))
    with open(INIT_FILE_PATH, 'w') as f:
        f.write(version_insert)

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

    with open(INIT_FILE_PATH, 'w') as f:
        f.write(original_init_content)
