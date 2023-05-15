#!/usr/bin/python3
# a Fabric script that generates a .tgz archive from the contents
import os
from datetime import datetime
from fabric.api import local
from fabric.context_managers import cd


def do_pack():
    """ create a tar file of a web static"""
    if os.path.isdir('./versions') is False:
        if local('mkdir versions').failed is True:
            return None

    dt = datetime.now()
    date_t = f"{dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}"
    filename = f"versions/web_static_{date_t}.tgz"

    if local(f'tar -czvf {filename} web_static').failed is True:
        return None
    return filename
