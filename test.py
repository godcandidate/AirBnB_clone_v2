#!/usr/bin/python3
"""Distributes an archive to your web servers"""
import os
from fabric.api import *
from datetime import datetime


env.hosts = ['3.84.239.114', '34.224.17.58']
def do_deploy(archive_path):
    """deploys the archive to the servers and updates it"""
    if not os.path.isfile(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        filename = os.path.basename(archive_path)
        fname = filename.split('.')[0]
        folder_name = '/data/web_static/releases/' + fname
        run('mkdir {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move content out of the sub-folder
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(fname, fname))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current on the
        # web server linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True
    except Exception:
        return False
