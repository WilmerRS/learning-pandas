import os
import pandas

from helpers.Path import Path


class ReadDataset:
    def __init__(self, path: str) -> None:
        self.path = path

    def read_csv(self) -> pandas.DataFrame:
        return pandas.read_csv(self.__get_full_path())

    def __get_full_path(self) -> str:
        root_path = Path.get_root_path()
        return os.path.join(root_path, 'assets', self.path)
