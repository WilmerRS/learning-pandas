import pandas

from helpers.Logger import Logger


class FormattingRule:
    def __init__(self, *, data_type, formatter, columns_to_apply):
        self.__data_type = data_type
        self.__formatter = formatter
        self.__columns_to_apply = columns_to_apply

    def format(self, dataset: pandas.DataFrame) -> pandas.DataFrame:
        rows = dataset.loc[:, self.__columns_to_apply]
        for column in rows:
            if not self.__isinstance(register=rows[column]):
                continue
            dataset[column] = rows[column].apply(lambda x: self.__formatter(x))
        return dataset

    def __isinstance(self, *, register):
        if self.__data_type == 'str':
            return register.dtype == 'object'
        if self.__data_type == 'number':
            return str(register.dtype).startswith('float') or str(register.dtype).startswith('int')

        return False

    def log(self):
        Logger.info(data={
            'type': self.__data_type,
            'columns': ','.join(self.__columns_to_apply)
        }, header=False, finish=False)
