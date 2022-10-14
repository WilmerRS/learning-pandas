import pandas
from helpers.Logger import Logger
from operations.Operator import Operator


class PrintHeadOperator(Operator):
    def execute(self, dataset: pandas.DataFrame, n=5) -> None:
        head = dataset.head(n=n)

        Logger.info(data=head, title='Head Operation')

        return None
