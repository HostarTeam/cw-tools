from bcrypt import checkpw

from cw_tools.util.common import hash_str

def test_hash_str():
    string = 'Hello world'
    hashed = hash_str(string)
    assert checkpw(string.encode(), hashed)