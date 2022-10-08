from pymysql import connect, OperationalError

from cw_tools.util.conf_parse import read_conf_file


def get_connection(path: str):
    db_conf = read_conf_file(path)
    try:
        return connect(**db_conf)
    except OperationalError as err:
        print(f'Error: Could not connect to database and got: {err.args[1]}')
        exit(1)
