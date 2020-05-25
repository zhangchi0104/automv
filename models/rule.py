import json
from models.matchers import Matcher
import shutil
# the basic Rule class
class Rule:
    """ Rule handles file moving based on the matcher
    """
    def __init__(self, rule_name: str, matcher: Matcher, destination: str):
        self._rule_name = rule_name
        self._matcher : Matcher = matcher
        self._destination = destination
        
    def run(self, file_name: str):
        if self._matcher.match(file_name):
            dst = self._move_file(file_name)
            print(f"moved {file_name} to {dst}")
        
    def _move_file(self, file_name: str) -> str:
           return shutil.move(file_name, self._destination)

    @property
    def name(self):
        return self._rule_name
    
# def check(self, filename: str) -> bool:
        

def load_rules_from_json(file_name: str) -> list: 
    res = []
    with open(file_name, 'r') as conf:
        configs: dict = json.load(conf)
        for rule_detail in configs['rules']:
            res.append(Rule(rule_detail))

    return res