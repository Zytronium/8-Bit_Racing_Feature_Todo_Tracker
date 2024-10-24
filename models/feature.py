"""
module for the Feature class
"""


class Feature:
    """
    class representing a feature to add to the game.
    name: feature name/short summary
    description: more detailed description of the feature
    est_scope: estimated time it will take to make the feature
    done: boolean of whether the feature is done or not
    """
    def __init__(self, name: str, description: str, est_scope: str, done: bool = False):
        self.name = name
        self.description = description
        self.est_scope = est_scope
        self.done = done
        # todo: add to list and save to json file

this_project = Feature("8-Bit Racing Feature Todo Tracker program",
                       "This project, aka 8-Bit Racing game feature todo list tracker in a python command line interpreter interface that allows for viewing, adding, modifying, or deleting feature ideas from a todo list.",
                       "3 to 8 hours",
                       False)

