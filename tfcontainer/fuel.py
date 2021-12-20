from typing import Tuple, Any

import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers


EPOCS = 100


def get_data() -> pd.DataFrame:
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    dataset = pd.read_csv(url, names=column_names,
                            na_values='?', comment='\t',
                            sep=' ', skipinitialspace=True)
    return dataset


def preprocess(dataset: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    dataset = dataset.dropna()
    dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
    dataset = pd.get_dummies(dataset, columns=['Origin'], prefix='', prefix_sep='')
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)
    train_features = train_dataset.copy()
    test_features = test_dataset.copy()
    train_labels = train_features.pop('MPG')
    test_labels = test_features.pop('MPG')
    return train_features, test_features, train_labels, test_labels



def linear_model() -> tf.keras.Sequential:
    normalizer = tf.keras.layers.Normalization(axis=-1)
    model = tf.keras.Sequential([
        normalizer,
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
        ])
    model.compile( optimizer=tf.optimizers.Adam(learning_rate=0.1), loss='mean_absolute_error')

    return model
    
def train(model, train_features, train_labels) -> Any:
    history = model.fit(
        train_features,
        train_labels,
        epochs=EPOCS,
        # Suppress logging.
        verbose=0,
        # Calculate validation results on 20% of the training data.
        validation_split = 0.2)
    return history


def model_test(model, test_features, test_labels):
    test_results = model.evaluate(test_features, test_labels, verbose=0)
    print(test_results)
    return test_results

if __name__ == '__main__':
    print('starting...')
    print('fetching data')
    dataset  = get_data()
    print('preprocessing the data')
    train_features, test_features, train_labels, test_labels = preprocess(dataset)
    print('creating a linear model')
    model = linear_model()
    print('training...')
    train(model, train_features, train_labels)
    print('test model...')
    model_test(model, test_features, test_labels)
    print('done')
