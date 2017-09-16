"""
Some basic utilities
"""

import six
import sys
import os
from subprocess import Popen, PIPE
from datetime import datetime


def __execute(*args):
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    return out, err, process.returncode


def safe_create(db_path):
    """Creates folder safely"""
    path = os.path.dirname(db_path)
    if not os.path.exists(path):
        os.mkdir(path)


def requires(*binaries):
    """checks for presence of given binaries"""
    for bin in binaries:
        out, err, ret = __execute("which", bin)
        if ret == 0:
            six.print_("{} not found , Please set the $PATH variable with {} path".format(bin, bin))
            sys.exit(2)


def download_website(domain):
    """download the domain with wget"""

    out, err, ret = __execute("wget", "--convert-links", "--recursive", domain)
    return ret == 0


def is_repo(path):
    """is repository path"""
    return os.path.exists(os.path.join(path, ".git"))


def git_init(path):
    """initialize git path if not exists"""
    if not is_repo(path):
        os.chdir(path)
        out, err, ret = __execute("git", "init")
        return ret == 0
    return True


def git_commit(path):
    """commit the downloaded changes"""
    os.chdir(path)
    add_out, add_err, add_ret = __execute("git", "add", ".")
    commit_out, commit_err, commit_ret = __execute("git", "commit", "-m", str(datetime.now()))
    return (add_ret + commit_ret) == 0


def is_exists(path):
    """path existance"""
    return os.path.exists(path)