#!/usr/bin/python3
from fabric.api import *
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    file = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file))

        return "versions/web_static_{}.tgz".format(file)

    except Exception as e:
        return None

env.hosts = ['3.84.239.114', '34.224.17.58']

def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.
    Args:
        archive_path (str): path of the .tgz file to transfer
    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = api.put(archive_path)
            if files.exists(outpath):
                api.run('rm -rdf {}'.format(outpath))
            run('mkdir -p {}'.format(outpath))
            run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            run('rm -f {}'.format(putpath[0]))
            run('mv -u {}/web_static/* {}'.format(outpath, outpath))
            run('rm -rf {}/web_static'.format(outpath))
            run('rm -rf /data/web_static/current')
            run('ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True

def deploy():
    """creates and distributes archive to  web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
