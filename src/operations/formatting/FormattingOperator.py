import pandas
from helpers.Logger import Logger
from operations.Operator import Operator
from operations.formatting.FormattingRule import FormattingRule


class FormattingOperator(Operator):
    def __init__(self, *, rules: list[FormattingRule]):
        self.__rules = rules

    def execute(self, dataset: pandas.DataFrame) -> None:
        formatted = dataset.loc[:]
        for rule in self.__rules:
            formatted = rule.format(dataset=formatted)
        return formatted

    def log(self):
        Logger.info(data='', title='Format rules to apply',
                    finish=False)
        for rule in self.__rules:
            rule.log()
