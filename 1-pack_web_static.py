#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    dt = datetime.now()
    date_t = f"{dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}"
    filename = f"versions/web_static_{date_t}.tgz"

    try:
        local("mkdir -p versions")
        local("tar -czvf {}.tgz".format(filename))
        return "{}.tgz".format(filename)

    except Exception as e:
        return None
