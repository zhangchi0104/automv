import json
from models.matchers import Matcher
import shutil
# the basic Rule class
class Rule(object):
    """ Rule handles file moving based on the json config

    Rule uses matcher to check the file name if the filename matches the pattern
    then moves it into the destination folder
    
    Attributes:
        name/:          the name provided in the config json file
        _matcher:       matchers for underlying rules
        _destination:   where the file should be sent

    """
    def __init__(self, rule_name: str, matcher: Matcher, destination: str):
        """ inits the Rule instance
        
        Args:
            rule_name:   the name of the rule
            matcher:     the matcher this Rule uses
            destination: the target folder file will be sent
        """
        self._rule_name = rule_name
        self._matcher : Matcher = matcher
        self._destination = destination
        
    def run(self, file_name: str):
        """ run the rule
        
        it first runs the matcher to check the file name
        if matches copy it to the folder

        Args:
            file_name: the name of the file

        """
        if self._matcher.match(file_name):
            dst = shutil.move(file_name, self._destination)
            print(f"moved {file_name} to {dst}")
        
    @property
    def name(self):
        return self._rule_name
