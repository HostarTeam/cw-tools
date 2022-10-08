from cw_tools.util.conf_parse import get_db_conf_from_conf


def test_get_db_conf_from_conf():
    conf = {
        'database': {
            'host': '195.133.95.113',
            'port': 3306,
            'user': 'cw',
            'database': 'cw',
            'password': 'Test1'
        }}
    db_conf = get_db_conf_from_conf(conf)
    assert db_conf.get('host')
    assert type(db_conf.get('port')) == int
    assert db_conf.get('user')
    assert db_conf.get('password')
