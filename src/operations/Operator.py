import abc

import pandas


class Operator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, *, dataset: pandas.DataFrame, **kwargs) -> any:
        raise "[BaseModel] Method without implementation"
