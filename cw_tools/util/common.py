from bcrypt import hashpw, gensalt


def hash_str(string: str, salt=gensalt(10)):
    return hashpw(string.encode(), salt)
