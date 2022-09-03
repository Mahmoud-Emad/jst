"""CMD, excute from command."""
import argparse
from jst.cmd.logger import Logger
from jst.cmd.manage import CommandManager


class JstCommandLine(object):
    """Command line handling to handle commands and excute from command."""

    def __init__(self, argv, *args, **kwargs) -> None:
        self.argv = argv
        self.path = None
        self.argsubparsers = None
        self.args = []
        self.looger = Logger()
        self.start()

    def start(self):
        argparser = argparse.ArgumentParser(description="Jsst version control takes at least 1 command.")
        argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
        argsubparsers.required = True
        self.argsubparsers = argsubparsers
        self.argparser = argparser
        self.initial_commands()
        self.parse_args(self.argparser, self.argv)

    
    def parse_args(self, initialized, argv):
        args = initialized.parse_args(argv)
        return self.echo(args)

    def initial_commands(self):
        self.new_command("init", help="Init command to initialize new repository.")
        self.new_command("add", help="add new files, changes to existing repository.")
        self.new_command("cat-file", help="Provide content of repository objects")

    def new_command(self, command, help):
        argsp = self.argsubparsers.add_parser(command, help=help)
        argsp.add_argument("path", metavar="directory", nargs="?", default=".", help="Where to create the repository.")
        return argsp

    def echo(self, args: argparse.Namespace):
        """echo command to forward arguments to excute method"""
        # self.looger.info('excuteing {} command.'.format(args.command))
        return self.excute(args)

    def excute(self, args: argparse.Namespace):
        """Escute and handle commands from cli."""
        if args.command in dir(CommandManager()):
            self.invoked_function = args.command
            excuted = getattr(CommandManager(), self.invoked_function)
            return excuted(args)
        else:
            self.looger.error("command '{}' not found.".format(args.command))
            return
