import os

import file_controller

class _PATHS:
    DB = file_controller.SYSTEM_PATHS["learning_db"]

    BEGINNER = os.path.join(DB, "beginner.json")

def pull_db_data(level: str) -> dict:
    """
    Pulls the database file and returns the data for
    which ever level given in args
    """
    level_attr = getattr(_PATHS, level.upper(), None)

    if level_attr is None:
        raise NotInPaths(f"{level}, not found in paths")

    return file_controller.pull_data(level_attr)

def get_card_titles(level: str) -> list:
    level_data = pull_db_data(level)

    titles = []

    for id in level_data:
        titles.append(level_data[id]["card_title"])

    return titles

class NotInPaths(Exception):
    pass