from typing import Any, Tuple
from pymysql import Connection, MySQLError, connect, OperationalError

from cw_tools.util.conf_parse import read_conf_file


def get_connection(path: str):
    db_conf = read_conf_file(path)
    try:
        return connect(**db_conf, autocommit=True)
    except OperationalError as err:
        print(f'Error: Could not connect to database and got: {err.args[1]}')
        exit(1)


def execute_query(conn: Connection,
                  query: str, args: Tuple[Any] = None):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, args)

            return cursor.fetchall()
    except MySQLError as err:
        print(
            f'Error: Could not execute sql query `{query}`,\
                got: `{err.args[1]}`')
        exit(1)
