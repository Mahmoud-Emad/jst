"""CMD, excute from command."""
import argparse
from jst.cmd.logger import Logger
from jst.cmd.manage import CommandManager




class CommandLine(object):
    """Command line handling to handle commands and excute from command."""
    def __init__(self, *args, **kwargs) -> None:
       self.path = None
       self.args = []
       self.initialized = False
       self.argsubparsers = None
       self.looger = Logger()

    def start(self):
        if not self.initialized:
            argparser = argparse.ArgumentParser(description="Jsst version control takes at least 1 command.")
            argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
            argsubparsers.required = True
            self.initialized = True
            self.argsubparsers = argsubparsers
            self.argparser = argparser
            return argparser
        return self.argparser
    
    def new_command(self, command, help):
        self.start()
        argsp = self.argsubparsers.add_parser(command, help=help)
        argsp.add_argument("path", metavar="directory",
            nargs="?", default=".",
            help="Where to create the repository."
        )
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
            self.looger.error('command \'{}\' not found.'.format(args.command))
            return
