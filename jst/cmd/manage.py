from jst.cmd.logger import Logger
from jst.structure.repository import JstRepository
import argparse, time


class CommandManager():
    def __init__(self) -> None:
        self.looger = Logger()

    def init(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '\'{}\' command.'.format(args.command))
        time.sleep(1)
        repo = JstRepository(args.path, force=True)
        return repo.create(args.path, args)

    def add(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('add command')

    def cat_file(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def checkout(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def hash_object(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def log(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def tree(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def merge(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rebase(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rev_parse(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def rm(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def show(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')

    def tag(self, args: argparse.Namespace):
        self.looger.success('Excuteing', '{} command.'.format(args.command))
        print('init command')