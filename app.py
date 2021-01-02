#!/usr/local/bin/python3
from smartmv.helpers import load_rules
from argparse import ArgumentParser
from smartmv.models.rule import Rule
from typing import List, TypedDict


class ParsedArgs(TypedDict):
    files: List[str]
    rule: str 

class App(object):
    def __init__(self, rules: List[Rule]):
        self._arg_parser = self._init_argument_parser()
        self._rules = rules 

    def _init_argument_parser(self) -> ArgumentParser:
        ap = ArgumentParser()
        ap.add_argument("files", metavar="file_name",
                    type=str, nargs='+', help="the name of the files")
        ap.add_argument("--rule", "-r", required=False, help="the specified rule", type=str)
        
        return ap

    def run(self):
        args: ParsedArgs = self._arg_parser.parse_args()
        files = args.files
        rule_name = args.rule

        for fn in files:
            self.process_file(fn, rule_name)

    def process_file(self, file_name: str, rule_name: str = None):
        """ process file matches names by iterating all the rules

        this function iterating through all the rules
        if there is a match the loop will be terminated early

        if the rule name is specified, will rum the specified rule

        Args:
            file_name: the name of the file
            rules: the dictonary contains all the rules indexed by their names
            rule_name(optional): the specifed rule name
        
        Returnes:
            None

        Raises: 
            KeyError: when the specified rule name is not in the dictionary

        """
        if rule_name:
            rules[rule_name].run(file_name)
        else:
            sorted_rules = sorted(self._rules.values(), key=lambda x: x.priority, reverse=True)
            for rule in sorted_rules:
                if rule.run(file_name):
                    return
      
      
if __name__ == "__main__":
    rules = load_rules('/Users/alexzhang/Projects/smartmv/config.json')
    app = App(rules)
    app.run()
