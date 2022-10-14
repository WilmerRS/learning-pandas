import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from helpers.ReadDataset import ReadDataset


class Cleaner:
    def __init__(self):
        pass

    def clean(self):
        read_dataset = ReadDataset('datasets/data.csv')
        df = read_dataset.read_csv()
        print('✅',df.shape)
        print('✅',df.head())

        df.drop(['item'], axis=1, inplace=True)
        df.drop(['importer_id'], axis=1, inplace=True)
        df.drop(['exporter_id'], axis=1, inplace=True)
        df.drop(['days_in_transit'], axis=1, inplace=True)

        sum = df['mode_of_transport'].duplicated().sum()
        print('🌀',sum)
        df.drop(['mode_of_transport'], axis=1, inplace=True)


        dummies = pd.get_dummies(df['route'], prefix='route')
        print('✅ Originals\n', df['route'])
        print('✅ Dummies\n', dummies)
        df = pd.concat([df, dummies], axis=1)
        df.drop(['route'], axis=1, inplace=True)

        dummies = pd.get_dummies(df['country_of_origin'], prefix='origin')
        df = pd.concat([df, dummies], axis=1)
        print('✏️ Originals\n', df['country_of_origin'])
        print('✏️ Dummies\n', dummies)
        df.drop(['country_of_origin'], axis=1, inplace=True)

        print('✅ Declared quantity\n', df['declared_quantity'])
        min_max_scaler = MinMaxScaler()
        df['declared_quantity'] = min_max_scaler.fit_transform(
            df['declared_quantity'].values.reshape(-1, 1))
        print('✅ Declared quantity\n', df['declared_quantity'])

        df['declared_cost'] = min_max_scaler.fit_transform(
            df['declared_cost'].values.reshape(-1, 1))

        df['weight_diff'] = (
            (df['actual_weight']-df['declared_weight']) / df['actual_weight']
        ).round(3)*100
        df['weight_diff'] = min_max_scaler.fit_transform(
            df['weight_diff'].values.reshape(-1, 1))

        df.drop(['declared_weight'], axis=1, inplace=True)
        df.drop(['actual_weight'], axis=1, inplace=True)

        df['date_of_arrival'] = pd.to_datetime(df['date_of_arrival'])
        df['date_of_departure'] = pd.to_datetime(df['date_of_departure'])

        df['days_diff'] = df['date_of_arrival'] - df['date_of_departure']
        df['days_diff'] = df['days_diff'] / np.timedelta64(1, 'D')
        df['days_diff'] = min_max_scaler.fit_transform(
            df['days_diff'].values.reshape(-1, 1)
        )

        df.drop(['date_of_arrival'], axis=1, inplace=True)
        df.drop(['date_of_departure'], axis=1, inplace=True)

        X = df.drop(['valid_import'], axis=1)
        y = df['valid_import']

        print(X.head())
