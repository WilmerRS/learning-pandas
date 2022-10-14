import pandas
from helpers.ReadDataset import ReadDataset
from operations.Operator import Operator


class NlfOffenseDataset:
    __dataset: pandas.DataFrame = None
    __NLF_OFFENSE_CSV = 'datasets/nfl_offense_week_3.csv'

    def __init__(self):
        self.__load_dataset()

    def __load_dataset(self):
        readDataset = ReadDataset(path=self.__NLF_OFFENSE_CSV)
        self.__dataset = readDataset.read_csv()

    def apply(self, operation: Operator, **kwargs):
        """
        Apply operation to dataset.
        """
        result = operation.execute(dataset=self.__dataset, **kwargs)
        return result

    def dataset(self) -> pandas.DataFrame:
        return self.__dataset
