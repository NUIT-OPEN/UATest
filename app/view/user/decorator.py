from saika import MetaTable

from .hard_code import MK_PUBLIC


def ignore_auth(f):
    MetaTable.set(f, MK_PUBLIC, True)
    return f
