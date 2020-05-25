from models.conditions import Condition
from abc import ABC, abstractmethod
class Matcher(ABC):
    """ Matcher matches multiple conditons

    Matcher aggregates multiple conditions
    it checks each condition by an overall condition

    Attributes:
        _conditions: series of conditions to be matched
    """
    def __init__(self, conditons:list):
        self._conditions = conditons

    @abstractmethod
    def match(self, file_name: str) -> bool:
        pass

    @property
    def conditions(self):
        return self._conditions

class AllConditionsMatcher(Matcher):
    def __init__(self, conditions: list):
        super().__init__(conditions)

    def match(self, file_name:str) ->bool:
        for condition in self.conditions:
            if not condition.check(file_name):
                return False

            return True
