import json
import shutil
import pathlib
import os

from smartmv.models.conditions import Condition
from smartmv.models.options import Options


# the basic Rule class
class Rule(object):
    """ Rule handles file moving based on the json config

    Rule uses matcher to check the file name if the filename matches the pattern
    then moves it into the destination folder

    Attributes:
        name:          the name provided in the config json file
        _matcher:       matchers for underlying rules
        _destination:   where the file should be sent

    """

    def __init__(self, rule_name: str, condition: Condition, destination: str, priority: int, options: dict = None):
        """ inits the Rule instance

        Args:
            rule_name:   the name of the rule
            matcher:     the matcher this Rule uses
            destination: the target folder file will be sent
        """
        self._rule_name = rule_name
        self._condition: Condition = condition
        self._destination = pathlib.Path(destination)
        self._options: Options = Options(options)
        self._priority = priority

    def run(self, file_name: str) -> bool:
        """ run the rule

        it first runs the matcher to check the file name
        if matches copy it to the folder

        Args:
            file_name: the name of the file
        """
        dest = self._destination
        if self._options.create_sub_dir_option:
            dest = self._options.create_sub_dir(self._destination, file_name)
        if self._condition.check(file_name):
            dst = shutil.move(file_name, dest)
            print(f"moved {file_name} to {dst}")
            return True

        return False

    @property
    def name(self):
        return self._rule_name

    @property
    def priority(self):
        return self._priority
