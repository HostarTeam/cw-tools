from subprocess import run
from pymysql import MySQLError, OperationalError
from typer import Typer

from cw_tools.util.db import get_connection


app = Typer()


@app.command('db:status')
def db_status(conf_file='/etc/container-workspaces/conf.json'):
    try:
        conn = get_connection(conf_file)
        conn.ping()
        print('OK')
    except OperationalError:
        print('Error: Could not connect to database')
    except MySQLError:
        print('Error: Connected to server but could not ping the connection')


@app.command('db:shell')
def db_info(conf_file='/etc/container-workspaces/conf.json'):
    try:
        conn = get_connection(conf_file)
        print(conn.db)
        run(['mysql', '-h', conn.host, '-u',
            conn.user, f'--password={conn.password.decode()}'])
    except OperationalError:
        print('Error: Could not connect to database')
