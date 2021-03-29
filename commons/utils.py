import os

from django.contrib.auth.hashers import make_password, get_hasher


def to_hex(string):
    output = ""
    for char in string:
        output += hex(ord(char)).split('0x')[1]
    return output


def hash_function(string):
    # TODO Use a secure hash
    hasher = get_hasher()
    return to_hex(hasher.encode(string, os.environ.get("HASH_TOKEN_SALT", "")))
