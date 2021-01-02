from smartmv.models.conditions import Condition

from typing import (
    Dict,
    List,
    Union,
    Tuple,
)

class ConjunctionCondition(Condition):
    """ sub class of Condition handles Conjuctions of to conditions

    Attributes:
        _left: the left hand side of the condition
        _right: the right hand side of the condition
        _type_name: the type of the conjunction, must be "and"/"or"

    Methods:
        check: check if the condition has been met
        _check_and: use and condition to check
        _check_or: user or condition to check
    """

    def __init__(self, conditions: Union[List[Condition], Tuple[Condition]], conj_type: str):   
        """
        Raise:
            ValueError: if conj_type is not one of "and" / "or"
        """
        if conj_type not in ("and", "or"):
            raise ValueError()
        super().__init__(ConjunctionCondition)
        self._left = conditions[0]
        self._right = conditions[1]
        self._type_name = conj_type
      
    def _check_and(self, filename: str)-> bool:
        return self._left.check(filename) and self._right.check(filename)

    def _check_or(self, filename: str) -> bool:
        return self._left.check(filename) or self._right.check(filename)

    def check(self, filename: str) -> bool:
        return getattr(self, "_check_"+self._type_name)(filename)