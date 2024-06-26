from json import load


def read_conf_file(path: str):
    try:
        with open(path) as conf_file:
            conf_dict = load(conf_file)
            return get_db_conf_from_conf(conf_dict)
    except OSError as err:
        print(f'Error: {err.filename}')
    except SyntaxError:
        print(f'Error: could not parse conf file at {path}')


def get_db_conf_from_conf(conf: dict):
    db_conf_dict = conf.get('database')
    return dict(host=db_conf_dict.get('host'),
                port=db_conf_dict.get('port'),
                user=db_conf_dict.get('user'),
                database=db_conf_dict.get('database'),
                password=db_conf_dict.get('password'))
