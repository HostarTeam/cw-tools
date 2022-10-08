from typing import Tuple
from pymysql import Connection
from tabulate import tabulate

from cw_tools.util.db import execute_query, get_connection


def list_clients(path: str):
    conn = get_connection(path)
    clients = fetch_clients(conn)
    pretty_print_clients(clients)


def fetch_clients(conn: Connection):
    sql = 'SELECT * FROM clients'
    return execute_query(conn, sql)


def pretty_print_clients(clients: Tuple[tuple]):
    print(tabulate(clients, headers=['ID', 'Hashed Secret']))
