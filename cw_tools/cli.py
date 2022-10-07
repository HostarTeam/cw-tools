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
        print('Error: Could not connect to database and ')
    except MySQLError:
        print('Error: Connected to server but could not ping the connection')


@app.command('db:nothing')
def db_nothing(conf_file='/etc/container-workspaces/conf.json'):
    pass
