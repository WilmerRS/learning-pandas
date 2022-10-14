from exercises.NlfOffenseDataset import NlfOffenseDataset
from exercises.Cleaner import Cleaner

from operations.formatting.FormattingOperator import FormattingOperator
from operations.formatting.FormattingRule import FormattingRule
from operations.plotter.PrintHeadOperator import PrintHeadOperator


def mainCleaner():
    print('\n\n🚀 Learning Pandas')
    cleaner = Cleaner()
    cleaner.clean()


def mainCompositionPandas():
    print('\n\n🚀 Learning Pandas')

    nlfOffenseDataset = NlfOffenseDataset()
    nlfOffenseDataset.apply(
        operation=PrintHeadOperator(),
        n=4,
    )

    formattingOperator = FormattingOperator(
        rules=[
            FormattingRule(
                data_type='str',
                formatter=lambda register: register.upper(),
                columns_to_apply=['team']
            ),
            FormattingRule(
                data_type='number',
                formatter=lambda register: register * 2,
                columns_to_apply=['rank']
            ),
        ]
    )
    formattingOperator.log()
    formattedDataset = nlfOffenseDataset.apply(operation=formattingOperator)
    print(formattedDataset)

    # Obtener conteo de nulos por columna
    # Filtrar nulos
    # Rellenar nulos con
    # formatting
    # replacing
    # splitting

    print('\n✅ Finish\n\n')


if __name__ == '__main__':
    mainCleaner()
    # mainCompositionPandas()
