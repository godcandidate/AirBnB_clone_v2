#!/usr/bin/python3
"""
Fabric script that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['3.84.239.114', '34.224.17.58']

def do_pack():
    """generates a tgz archive"""
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        ext = file_n.split(".")[0]
        new_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file,new_ path, ext))
        run('rm /tmp/{}'.format(file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(new_path, ext))
        run('rm -rf {}{}/web_static'.format(new_path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(new_path, ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
