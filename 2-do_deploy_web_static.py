#!/usr/bin/python3
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric.api import *
from fabric.contrib import files
import os


env.hosts = ['3.84.239.114', '34.224.17.58']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/alx_server'


def deploy_archive(archive_path):
    """Function to transfer `archive_path` to web servers.
    Args:
        archive_path (str): path of the .tgz file to transfer
    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with cd('/tmp'):
        file_name = os.path.basename(archive_path)
        new_path, ext = os.path.splitext(file_name)
        try:
            put_path = put(archive_path)
            if files.exists(new_path):
                run('rm -rdf {}'.format(new_path))
            run('mkdir -p {}'.format(new_path))
            run('tar -xzf {} -C {}'.format(put_path[0], new_path))
            run('rm -f {}'.format(put_path[0]))
            run('mv -u {}/web_static/* {}'.format(new_path, new_path))
            run('rm -rf {}/web_static'.format(new_path))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(new_path))
            print('New version deployed!')
        except:
            return False
        else:
            return True

