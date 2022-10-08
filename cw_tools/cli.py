from subprocess import run
from click import confirm
from pymysql import MySQLError
from typer import Option, Typer
from cw_tools.util.common import generate_random_string

from cw_tools.util.db import get_connection
from cw_tools.util import clients


app = Typer()


@app.command('db:status')
def db_status():
    try:
        conn = get_connection()
        conn.ping()
        print('OK')
    except MySQLError:
        print('Error: Connected to server but could not ping the connection')


@app.command('db:shell')
def db_info():
    conn = get_connection()
    run(['mysql', '-A', '-h', conn.host, '-u',
        conn.user, f'--password={conn.password.decode()}', '-D',
        conn.db.decode()])


@app.command('clients:list')
def clients_list():
    clients.list_clients()


@app.command('clients:create')
def clients_create(
    id: str =
    Option(
        None,
        help='If not specified, will be randomally generated'),
    secret: str =
    Option(
        None,
        help='If not specified, will be randomally generated')):
    if id is None:
        id = generate_random_string(32)
        print(f'Client ID was not specified, so it was generated: {id}')
    if secret is None:
        secret = generate_random_string(32)
        print(
            f'Client Secret was not specified, so it was generated: {secret}')
    clients.create_client(id, secret)
    print('Added client successfully')


@app.command('clients:delete')
def clients_delete(id: str):
    client = clients.get_client(id)
    if client is None:
        print(f'Error: No such client with ID: {id}')
        exit(1)

    if not confirm(f'Are you sure you want to delete client with ID: {id}?',
                   default=False):
        print('Aborting...')
        exit(1)

    clients.delete_client(id)
    print(f'Successfully deleted client with ID {id}')
