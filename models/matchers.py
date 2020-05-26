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
        """check if the filename matches the conditon
        
        Args:
            file_name: the name of the file to be matched

        Returns:
            True if the file name mateches the condtions
            otherwise False
        """
        pass

    @property
    def conditions(self):
        return self._conditions

class AllConditionsMatcher(Matcher):
    """  AllConditionsMatcher matches all the conditions provided for the file

    i.e. condition1 and condition2 and condition3...

    """
    def __init__(self, conditions: list):
        super().__init__(conditions)

    def match(self, file_name:str) ->bool:
        """ checks if the file name matches all the condition"""
        for condition in self.conditions:
            if not condition.check(file_name):
                return False

            return True

class AnyConditionMatcher(Matcher):

    def __init__(self, conditions):
        super().__init__(conditions)
    
    def match(self, file_name: str) -> bool:
        for condition in self.conditions:
            if not condition.check(file_name):
                return True
            
        return False 
