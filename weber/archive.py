"""

Archives websites an individual folder in git 
repositories

"""

import os
from os.path import expanduser
import utils
import time
import six
import Queue


class Archive(object):
    """Primary archival folder to set up on particular place
       In this system
    """

    _commit_file_path = expanduser("~/.weber/webcommit.txt")
    _data_path = expanduser("~/.weber/data/")

    def __init__(self, domains=[]):
        self.path = self.__class__._data_path
        self.domains = domains
        self.d_q = Queue.Queue()
        for domain in self.domains:
            self.d_q.put(domain)

    @classmethod
    def initialize(cls):
        utils.git_init(cls._data_path)

    def add(self, domain):
        self.domains.append(domain)
        self.d_q.put(domain)
        os.chdir(self.path)
        utils.download_website(domain)
        self.__class__.commit(self.domains)

    def list(self):
        return os.listdir(self.path)

    @classmethod
    def commit(cls, domains):
        if not utils.is_exists(cls._commit_file_path):
            utils.safe_create(cls._commit_file_path)
        fp = open(cls._commit_file_path, "w")
        fp.write("\n".join(domains))
        fp.close()

    @classmethod
    def load(cls):
        domains = open(cls._commit_file_path).read().split("\n")
        return cls(domains=domains)

    @classmethod
    def is_initalized(cls):
        return utils.is_exists(cls._data_path) and utils.is_exists(cls._commit_file_path)

    @classmethod
    def create_data_dir(cls):
        utils.safe_create(cls._data_path)

    def __iter__(self):
        return self.list()

    def download(self):
        while not self.d_q.empty():
            domain = self.d_q.get()
            if domain == "":
                continue
            six.print_("downloading current verions for {}".format(domain))
            if utils.download_website(domain):
                six.print_("Downloded successfully")
            else:
                six.print_("Download Error")
            time.sleep(5)
        utils.git_commit(self.path)
        self.__class__.commit(self.domains)