import yaml


def read_config(config_path: str) -> dict:
    """
    Reads config from .yaml file.
    :param config_path: path to .yaml file to load from

    :return: configuration dictionary

    """
    with open(config_path, "rb") as f_in:
        config = yaml.safe_load(f_in)
    return config


def parse_config(config: dict) -> dict:
    """
    Parses the configuration dictionary.
    :param config: configuration dictionary

    :return: configuration parameters
    """
    params = dict()
    params['input_data_path'] = config['input_data_path']
    params['output_encoder_path'] = config['output_encoder_path']
    params['output_scaler_path'] = config['output_scaler_path']
    params['output_model_path'] = config['output_model_path']
    params['metric_path'] = config['metric_path']
    params['split_test_size'] = config['splitting_params']['test_size']
    params['split_random_state'] = config['splitting_params']['random_state']

    params['model_type'] = config['train_params']['model_type']
    params['model_random_state'] = config['train_params']['random_state']
    params['solver'] = config['train_params']['solver']
    params['penalty'] = config['train_params']['penalty']
    params['model_C'] = config['train_params']['C']
    params['threshold'] = config['threshold']

    return params
