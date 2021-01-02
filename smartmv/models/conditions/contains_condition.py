from smartmv.models.conditions import Condition

class ContainsCondition(Condition):
    """  ContainsKeywordCondition checks if a file name contians the condition
    
    Attributes:
        _keywords: the keywords should be contained
    
    """

    def __init__(self, keywords):
        """ inits ContainsKeywordCondition 
        with condition type and a list of keywords
        """
        super().__init__('contains')
        self._keywords = keywords

    def check(self, file_name: str) -> bool:
        """ checks if a file name contains any key word"""
        for keyword in self._keywords:
            if keyword in file_name:
                return True
        return False