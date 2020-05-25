import json 
from models.conditions import *
from models.matchers import *
from models.rule import Rule

def load_config(config_path: str) -> (str, dict):
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
    res = []
    for condition in conditions:
        if condition['type'] == 'contains':
            res.append(ContainsKeywordCondition(condition['keywords']))

    return res

def _generate_rule(rule_json: dict) -> Rule:
    matcher = None
    conditions = _parse_conditions(rule_json['conditions'])
    if rule_json['matchType'] == 'all':
       matcher = AllConditionsMatcher(conditions)
    
    rule = Rule(rule_json['name'],  matcher, rule_json['destination'])
    return rule
        