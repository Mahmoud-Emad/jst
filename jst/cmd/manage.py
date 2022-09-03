import os
from jst.cmd.logger import Logger
from jst.structure.objects import JstObject, obj_cat_file, object_find, object_hash
from jst.structure.repository import JstRepository
import argparse, time

from jst.utils.log_graphviz import log_graphviz


class CommandManager():
    def __init__(self, args) -> None:
        self.logger = Logger()
        repo = JstRepository(args.path, force=True)
        self.repo = repo

    def init(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '\'{}\' command.'.format(args.command))
        time.sleep(1)
        return self.repo.create(args.path, args)
    
    def validate_repo(self, args, path='.'):
        """Validate the repository"""
        path = os.path.realpath(path)
        if self.repo or os.path.isdir(os.path.join(path, ".jst")):
            return True
        else:
            self.logger.error(
                'Excuteing',
                '\'{}\' command can calling after initializeing repository.'
                .format(args.command)
            )
        return False

    def add(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('add command')

    def cat_file(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        time.sleep(1)
        if self.repo.repo_find():
            obj_cat_file(
                self.repo,
                args.object, fmt=args.type.encode()
            )

    def checkout(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def hash_object(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        if args.write:
            repo = JstRepository(".")
        else:
            repo = None
        with open(args.path, "rb") as fd:
            sha = object_hash(fd, args.type.encode(), repo)
            print(sha)

    def log(self, args: argparse.Namespace):
        # self.logger.success('Excuteing', '{} command.'.format(args.command))
        print("digraph wyaglog{")
        log_graphviz(self.repo, object_find(self.repo, args.commit), set())
        print("}")
        # repo = JstRepository(".").repo_find()
        # print(repo)
        # # self.logger.doc('Log: digraph JstLog{', log_graphviz(repo, object_find(repo, args.commit), set()))
        # self.logger.doc('}', '')

    def tree(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def merge(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rebase(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rev_parse(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rm(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def show(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def tag(self, args: argparse.Namespace):
        self.logger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')