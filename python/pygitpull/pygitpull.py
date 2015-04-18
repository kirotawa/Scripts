#!/usr/bin/python

import re
import os
import sys

HOME = os.getenv("HOME")
rgxp_motor = re.compile(r"\* \w+")
search = rgxp_motor.search

try:
    import git as _git
except ImportError:
    print "You need to installl python-git"
    sys.exit(1)


def get_branch(git):
    branches = git.branch()
    branches = branches if branches else 'None'
    result = search(branches)
    branch = result.group() if result else None
    return branch.split('* ')[1] if branch else 'no branch'


def checkout_to_master(git, branch):
    try:
        print "Checkouting from %s to master" % (branch)
        git.checkout("master")
        ret = "master"
    except _git.GitCommandError:
        print "Could not change branch to master"
        ret = branch

    return ret


def exec_pulls(dirs):
    for dir in dirs:
        primary_path = HOME+'/'+dir
        for gitrepo in os.listdir(primary_path):
            full_path = primary_path+'/'+gitrepo
            if os.path.isdir(full_path):
                if '.git' in os.listdir(full_path):
                    try:
                        print "Repository %s" % full_path.split('/')[-1]
                        git = _git.cmd.Git(full_path)
                        branch = get_branch(git)

                        if branch != "master":
                            branch = checkout_to_master(git, branch)

                        print "git pull in %s in branch %s" % (full_path,
                                                               branch)
                        git.pull()
                        print "done"
                    except _git.GitCommandError:
                        print "Error not a git repository or a valid remote"

if __name__ == '__main__':
    dirs = sys.argv[1:]
    if not dirs:
        print "Usage: pygitpull <root_git_directories>"
        sys.exit(0)

    exec_pulls(dirs)
