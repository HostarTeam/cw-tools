from subprocess import run
from pymysql import MySQLError
from typer import Typer

from cw_tools.util.db import get_connection
from cw_tools.util.clients import list_clients


app = Typer()


@app.command('db:status')
def db_status(conf_file='/etc/container-workspaces/conf.json'):
    try:
        conn = get_connection(conf_file)
        conn.ping()
        print('OK')
    except MySQLError:
        print('Error: Connected to server but could not ping the connection')


@app.command('db:shell')
def db_info(conf_file='/etc/container-workspaces/conf.json'):
    conn = get_connection(conf_file)
    run(['mysql', '-h', conn.host, '-u',
        conn.user, f'--password={conn.password.decode()}', '-D',
        conn.db.decode()])


@app.command('clients:list')
def clients_list(conf_file='/etc/container-workspaces/conf.json'):
    list_clients(conf_file)
