from models.conditions import Condition

class ExtensionCondition(Condition):
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