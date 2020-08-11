import re
from pathlib import Path


class Options(object):
    """Options abstracts the 'options' in json config

    It configs reads the parsed json object and stores the values
    as attributes. Methods are inplemented in this class to manipulate
    those values

    Attributes
        sub_dir: if user want to create new sub dir inside directory 
            None: not specified
            str: Indicate the name of the folder
            Regex: the format of the folder that based on the file to be moved. wraped with "%" 

    """

    def __init__(self, options: dict):
        if options is None:
            options = {}
        options.setdefault('createSubDir', None)
        self._sub_dir_option: str = options['createSubDir']

    def create_sub_dir(self, destination: Path, file_name: str) -> Path:
        """ create sub dir if it doesnt exists as configed

        Args:
            destination: the destination dir configed in 'rule'
            file_name: the name of the file to be moved

        Raises:
            FileNotFoundError: if destination does not exist

        """
        if self._sub_dir_option == None or self._sub_dir.isspace():
            return
        if self._sub_dir_option[0] == '%' and self._sub_dir_option [-1] == '%':
            pattern = re.compile(self._sub_dir.strip('%'))
            dir_name = pattern.findall(file_name)[0]
            destination.mkdir(dir_name, exist_ok=True)

        return destination/dir_name

    @property
    def create_sub_dir_option(self):
        return self._sub_dir_options
