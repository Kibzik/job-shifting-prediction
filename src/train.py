import sys
import logging
import json
import pickle
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from config_reader import read_config, parse_config
from models.model_actions import train_model, predict_model, evaluate_model

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def train_processing(config_path: str = "../config/train_config.yaml"):
    """
    Transform data, train and evaluate model and store the artifacts.
    :param config_path: training parameters

    :return: nothing

    """
    config = read_config(config_path)
    training_params = parse_config(config)

    logger.info('Reading data...')
    df = pd.read_csv(training_params['input_data_path'])
    logger.info(f'Initial dataset shape: {df.shape}.')

    logger.info('Validation of the initial dataset...')
    logger.info('   Drop columns...')
    df.drop(['EmployeeCount', 'Over18', 'StandardHours'], axis=1, inplace=True, errors='ignore')
    logger.info('   Encode target variable...')
    df["Attrition"].replace(['No', 'Yes'],
                            [0, 1], inplace=True)
    logger.info('Dataset was successfully validated.')

    X = df.drop('Attrition', axis=1)
    y = df['Attrition']

    logger.info('Splitting dataset into training and test parts...')
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=training_params['split_test_size'],
                                                        shuffle=True,
                                                        random_state=training_params['split_random_state'])
    logger.info(f'  Training dataset shape: {X_train.shape}, test part shape: {X_test.shape}.')
    logger.info('Done.')

    logger.info('One-hot encoding...')
    train_dict = X_train.to_dict(orient='records')
    test_dict = X_test.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    dv.fit(train_dict)

    X_train = dv.transform(train_dict)
    X_test = dv.transform(test_dict)
    logger.info('One-hot encoding done.')

    logger.info('Feature scaling...')
    min_max = MinMaxScaler()
    min_max.fit(X_train)
    X_train_scaled = min_max.transform(X_train)

    X_test_scaled = min_max.transform(X_test)
    logger.info('Fs done.')

    logger.info(f"Starting train model with the following params: {training_params}.")
    logger.info('   Training the model...')
    model = train_model(X_train_scaled, y_train, training_params)
    model_name = type(model).__name__
    y_pred_train, probes_train = predict_model(model, X_train_scaled, training_params)
    train_metrics = evaluate_model(y_train, y_pred_train)
    logger.info(f'{model_name} metrics on training data: {train_metrics}')

    logger.info('Testing the model...')
    y_pred_test, probes_test = predict_model(model, X_test_scaled, training_params)
    test_metrics = evaluate_model(y_test, y_pred_test)
    logger.info(f'{model_name} metrics on test data: {test_metrics}')

    logger.info('Confusion matrix for the test data:\n')
    logger.info(confusion_matrix(y_test, y_pred_test))

    logger.info(f'\nSaving metrics to {training_params["metric_path"]} file...')
    with open(training_params['metric_path'], 'w') as metric_file:
        json.dump(test_metrics, metric_file)

    logger.info(f'Saving encoder to {training_params["output_encoder_path"]} file...')
    with open(training_params['output_encoder_path'], 'wb') as encoder_file:
        pickle.dump(dv, encoder_file)

    logger.info(f'Saving scaler to {training_params["output_scaler_path"]} file...')
    with open(training_params['output_scaler_path'], 'wb') as scaler_file:
        pickle.dump(min_max, scaler_file)

    logger.info(f'Saving training model to {training_params["output_model_path"]} file...')
    with open(training_params['output_model_path'], 'wb') as model_file:
        pickle.dump(model, model_file)

    logger.info('Done.')


if __name__ == "__main__":
    train_processing()
