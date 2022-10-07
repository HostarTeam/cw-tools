import pymysql

from cw_tools.util.conf_parse import read_conf_file


def get_connection(path: str):
    db_conf = read_conf_file(path)
    return pymysql.connect(host=db_conf.host,
                           user=db_conf.user,
                           database=db_conf.db,
                           password=db_conf.password)
