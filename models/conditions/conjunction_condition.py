from models.conditions import Condition

from typing import (
    Dict,
    List,
    Union,
    Tuple
)

class ConjunctionCondition(Condition):

    def __init__(self, conditions: Union[List[Condition], Tuple[Condition]], conj_type: str):
        if conj_type not in ("and", "or"):
            raise ValueError()
        super().__init__(ConjunctionCondition)
        self._left = conditions[0]
        self._right = conditions[1]
        self._type_name = conj_type
      
    def _check_and(self, filename: str):
        return self._left.check(filename) and self._right.check(filename)

    def _check_or(self, filename: str):
        return self._left.check(filename) and self._right.check(filename)

    def check(self, filename: str):
        return getattr(self, "_check_"+self.type_name)(filename)