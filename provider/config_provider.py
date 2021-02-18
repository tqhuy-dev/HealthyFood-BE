import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    print(config.get('APP', 'ENVIRONMENT'))
    return config
