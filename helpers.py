import json 
from models.conditions import *
from models.matchers import *
from models.rule import Rule

def load_config(config_path: str) -> (str, dict):
    """ load config from json

    Args:
        config_path: the path of hte config file 
    
    Returns:
        the default rule name and a dict index by rule name contains all the rule

    Raises:
        IOError: if path does not exists or no permission
         
    """
    rules = {}
    default_rule = None
    with open(config_path, "r") as fp:
        configs: dict = json.load(fp)
        for rule_json in configs['rules']: 
            rule = _generate_rule(rule_json)
            rules[rule.name] = rule
        default_rule = configs['defaultRule']
    return (default_rule, rules)


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
    
    rule = Rule(rule_json['name'],  matcher, rule_json['destination'])
    return rule
        