from abc import ABC, abstractmethod


class Condition(ABC):
    """ Abstract class for Condition, 

    New condition type should use this class as base case.
    This class shall be aggregated by a Matcher.

    Attributes:
        type_name: indicates the type of the condition

    """

    def __init__(self, type_name: str):
        self._type_name = type_name

    @abstractmethod
    def check(self, file_name: str) -> bool:
        """
        check if the file name matches the condition

        Args:
            file_name: the file name to be checked

        Returns:
            True if the file name matches the condition
            otherwise False
        """
        return False

    @property
    def type_name(self) -> str:
        return self._type_name


class ContainsKeywordCondition(Condition):
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


class FileExtensionCondition(Condition):
    """
    Check if a file has certain extensions

    Attributes:
        _extensions: a list of extensions to be matched
    """
    def __init__(self, extensions: list):
        super().__init__('extension')
        self._extensions = extensions

    def check(self, file_name: str) -> bool:
        if '.' not in file_name: 
            return False
        elif file_name[0] == '.':
            return False

        for ext in self._extensions:
            if file_name.endswith(ext):
                return True
        
        return False
