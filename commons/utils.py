import os

from django.contrib.auth.hashers import get_hasher


def hash_function(string):
    hasher = get_hasher()
    return hasher.encode(string, os.environ.get("HASH_TOKEN_SALT", ""))
