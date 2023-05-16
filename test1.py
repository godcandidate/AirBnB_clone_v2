#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['3.84.239.114', '34.224.17.58']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension>
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, archive_no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Move files out of the web_static folder
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(archive_no_ext, archive_no_ext))

        # Remove the empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_no_ext))

        return True

    except Exception as e:
        print(e)
        return False

