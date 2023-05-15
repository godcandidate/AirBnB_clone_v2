#!/usr/bin/python3
import os
import re
from fabric.api import *


env.hosts = ['3.84.239.114', '34.224.17.58']

def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    try:
        if not (path.exists(archive_path)):
            return False

        # upload to server
        put(archive_path, /tmp/)

        # extracting name without extension
        pattern = r"(\w+)\.\w+"
        new_filename = re.search(pattern, archive_path).group(1)
        tmp_path = re.search(pattern, archive_path).group()

        # creating folder path
        new_path = '/data/web_static/releases/{}'.format(new_filename)
        run(f'mkdir -p {}'.format(new_path))

        # uncompress the archive
        run('tar -xzf /tmp/{} -C {}'.format(tmp_path, new_path))

        # delete archive
        run(f'rm /tmp/{}'.format(tmp_path))

        # delete symbolic
        run('rm /data/web_static/current')

        # create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(new_path))

        return True

    except e:
        return False
