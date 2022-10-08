from random import choices
from string import ascii_letters
from bcrypt import hashpw, gensalt


def hash_str(string: str, salt=gensalt(10)):
    return hashpw(string.encode(), salt)


def generate_random_string(length: int = 32):
    return ''.join(choices(ascii_letters, k=length))
