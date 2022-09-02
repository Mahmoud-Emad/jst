import argparse
from jst.utils.configration_parser import repo_default_config
from jst.cmd.logger import Logger
import os, configparser, time




class JstRepository(object):
    """A jst repository"""
    worktree = None
    jstdir = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.jstdir = os.path.join(path, ".jst")
        self.logger = Logger()

        if not (force or os.path.isdir(self.jstdir)):
            self.logger.error(
                "Failed!", "Not a jst repository %s" % path
            )
            return

        # Read configuration file in .jst/config
        self.conf = configparser.ConfigParser()
        cf = self.repo_file(self, "config")

        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception("Unsupported repositoryformatversion %s" % vers)
    
    def repo_path(self, repo, *path):
        """Compute path under repo's jstdir."""
        return os.path.join(repo.jstdir, *path)
    
    def repo_file(self, repo, *path, mkdir=False):
        """ 
            Same as repo_path, but create dirname(*path) if absent.  For
            example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
            .jst/refs/remotes/origin.
        """

        if self.repo_dir(repo, *path[:-1], mkdir=mkdir):
            return self.repo_path(repo, *path)
    
    def repo_dir(self, repo, *path, mkdir=False):
        """Same as repo_path, but mkdir *path if absent if mkdir."""

        path = self.repo_path(repo, *path)

        if os.path.exists(path):
            if (os.path.isdir(path)):
                return path
            else:
                raise Exception("Not a directory %s" % path)

        if mkdir:
            self.logger.header("Created directory", "%s"% path)
            os.makedirs(path)
            return path
        else:
            return None
    
    def create(self, path: str, args: argparse.Namespace):
        """Create a new repository at path."""

        repo = JstRepository(path, True)

        # First, we make sure the path either doesn't exist or is an
        # empty dir.

        if os.path.exists(repo.worktree):
            if not os.path.isdir(repo.worktree):
                raise Exception ("%s is not a directory!" % path)
            if os.listdir(repo.worktree):
                return self.logger.error(
                    "Failed!", "%s is not empty!" % path
                )
        else:
            os.makedirs(repo.worktree)

        assert(self.repo_dir(repo, "branches", mkdir=True))
        assert(self.repo_dir(repo, "objects", mkdir=True))
        assert(self.repo_dir(repo, "refs", "tags", mkdir=True))
        assert(self.repo_dir(repo, "refs", "heads", mkdir=True))

        # .jst/description
        with open(self.repo_file(repo, "description"), "w") as f:
            self.logger.header("Created file", "%s/.jst/description" %repo.worktree)
            description = "Unnamed repository; edit this file 'description' to name the repository.\n"
            f.write(description)

        # .jst/HEAD
        with open(self.repo_file(repo, "HEAD"), "w") as f:
            self.logger.header("Created file", "%s/.jst/HEAD" %repo.worktree)
            f.write("ref: refs/heads/master\n")

        with open(self.repo_file(repo, "config"), "w") as f:
            config = repo_default_config()
            config.write(f)
        self.logger.success('Successfully', 'created repository in \'{}\' dir.'.format(args.path))
        return repo