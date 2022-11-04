import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
)


def train_model(
    features: pd.DataFrame, target: pd.Series, training_params: dict):
    """
    Trains the model.
    :param features: features to train on
    :param target: target labels to train on
    :param training_params: training parameters
    :return: save model via pickle

    """
    if training_params['model_type'] == 'LogisticRegression':
        model = LogisticRegression(
            solver=training_params['solver'],
            penalty=training_params['penalty'],
            C=training_params['model_C'],
            random_state=training_params['model_random_state'],
            n_jobs=-1,
            verbose=1
        )
    else:
        raise NotImplementedError()

    model.fit(features, target)
    return model


def predict_model(model, features: pd.DataFrame, training_params: dict) -> [np.ndarray, np.ndarray]:
    """
    Makes predictions using model.
    :param model: the model to predict with
    :param features: the features to predict on
    :return: pipeline predictions

    """
    predict_probes = model.predict_proba(features)[:, 1]
    predicts = predict_probes >= training_params["threshold"]
    return [predicts, predict_probes]


def evaluate_model(target: pd.Series, predicts: np.array) -> dict:
    """
    Evaluates model predictions and returns the metrics.
    :param target: actual target labels
    :param predicts: pipeline hard predictions
    :param predict_probes: pipeline soft predictions
    :return: a dict of metrics in format {'metric_name': value}

    """
    # build confusion matrix
    accuracy = round(accuracy_score(target, predicts), 3)
    precision = round(precision_score(target, predicts, average='binary'), 3)
    recall = round(recall_score(target, predicts, average='binary'), 3)
    f1 = round(f1_score(target, predicts, average='binary'), 3)
    roc_auc = round(roc_auc_score(target, predicts, average='weighted'), 3)

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'ROC_AUC': roc_auc
    }
