import versioning

if __name__ == "__main__":

    currentVersion = versioning.get_version()
    nextVersion = currentVersion.bump_minor()
    versioning.save_version(nextVersion)
