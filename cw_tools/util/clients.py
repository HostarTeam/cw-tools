from typing import Tuple
from pymysql import Connection
from tabulate import tabulate
from cw_tools.util.common import hash_str

from cw_tools.util.db import execute_query, get_connection


def list_clients():
    conn = get_connection()
    clients = fetch_clients(conn)
    pretty_print_clients(clients)


def fetch_clients(conn: Connection):
    sql = 'SELECT * FROM clients'
    return execute_query(conn, sql)


def pretty_print_clients(clients: Tuple[tuple]):
    print(tabulate(clients, headers=['ID', 'Hashed Secret']))


def create_client(id: str, secret: str):
    conn = get_connection()
    sql = 'INSERT INTO clients(client_id, client_secret)'\
        'VALUES(%s, %s)'
    execute_query(conn, sql, (id, hash_str(secret)))


def get_client(conn: Connection, id: str):
    sql = 'SELECT * FROM clients WHERE client_id = %s'
    result = execute_query(conn, sql, id)
    if len(result) > 0:
        return result[0]

    return None


def delete_client(id: str):
    conn = get_connection()
    sql = 'DELETE FROM clients WHERE client_id = %s'
    execute_query(conn, sql, id)
