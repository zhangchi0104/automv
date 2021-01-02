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


