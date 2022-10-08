from typing import Tuple
from pymysql import MySQLError, Connection
from cw_tools.util.db import get_connection
from tabulate import tabulate


def list_clients(path: str):
    conn = get_connection(path)
    clients = fetch_clients(conn)
    pretty_print_clients(clients)


def fetch_clients(conn: Connection):
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM clients'
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except MySQLError as err:
            print(
                f'Error: Could not execute sql query `{sql}`,\
                 got: `{err.args[1]}`')


def pretty_print_clients(clients: Tuple[tuple]):
    print(tabulate(clients, headers=['ID', 'Hashed Secret']))
