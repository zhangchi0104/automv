
import json 
from models.conditions import *
from models.matchers import *
from models.rule import Rule

def load_rules(config_path: str) -> dict:
    """ load rules from json

    Args:
        config_path: the path of hte config file 
    
    Returns:
        A dict index by rule name contains all the rule

    Raises:
        IOError: if path does not exists or no permission
         
    """
    rules = {}

    with open(config_path, "r") as fp:
        configs: dict = json.load(fp)
        for rule_json in configs['rules']: 
            rule = _generate_rule(rule_json)
            rules[rule.name] = rule
       
    return rules


def _parse_conditions(conditions: list) -> list:
    """ parses conditions from json dictionary

    Args:
        conditions:
        list of conditons from json
    
    Returns:
        A list of rules parsed from json
    """
    res = []
    for condition in conditions:
        if condition['type'] == 'contains':
            res.append(ContainsKeywordCondition(condition['keywords']))
        elif condition['type'] == 'extension':
            res.append(FileExtensionCondition(condition['extensions']))

    return res

def _generate_rule(rule_json: dict) -> Rule:
    """ generate rules from json
    this function first generate conditions
    then genereate a matcher for the conditions
    then wrap it with a rule

    Args:
        rule_json: a dictionary from json represents a rule
    
    Returns: 
        A Rule instance from json
        
    """
    switch = {
        "all": lambda condition: AllConditionsMatcher(condition), 
        "any": lambda condition: AnyConditionMatcher(condition)
    }
    matcher = None
    conditions = _parse_conditions(rule_json['conditions'])
 
    matcher = switch[rule_json['matchType']](conditions)
    rule = Rule(rule_json['name'],  matcher, rule_json['destination'], rule_json["priority"])
    return rule

def process_file(file_name: str,  rules: dict, rule_name: str = None):
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
        sorted_rules = sorted(rules.values(), key= lambda x: x.priority, reverse=True)
        for rule in rules.values():
            if rule.run(file_name):
                return