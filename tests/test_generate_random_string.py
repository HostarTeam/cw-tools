from cw_tools.util.common import generate_random_string


def test_generate_random_string():
    length = 32
    result = generate_random_string(length)
    assert type(result) == str
    assert len(result) == length
