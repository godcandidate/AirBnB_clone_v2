#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['3.84.239.114', '34.224.17.58']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    my_archives = sorted(os.listdir("versions"))
    [my_archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(item)) for item in my_archives]

    with cd("/data/web_static/releases"):
        my_archives = run("ls -tr").split()
        my_archives = [a for a in archives if "web_static_" in a]
        [my_archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(item)) for item in my_archives]
