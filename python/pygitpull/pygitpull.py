#!/usr/bin/python

import os
import sys

HOME = os.getenv("HOME")

try:
    import git
except ImportError:
    print "You need to installl python-git"
    sys.exit(1)


def exec_pulls(dirs):
    for dir in dirs:
        primary_path = HOME+'/'+dir
        for gitrepo in os.listdir(primary_path):
            full_path = primary_path+'/'+gitrepo
            if os.path.isdir(full_path):
                if '.git' in os.listdir(full_path):
                    print "git pull in %s" % full_path
                    git_pull = git.cmd.Git(full_path)
                    git_pull.pull()
    print "done"

if __name__ == '__main__':
    dirs = sys.argv[1:]
    exec_pulls(dirs)
