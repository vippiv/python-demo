from flask import g


def login_log():
    print("%s" % g.username)
    pass
