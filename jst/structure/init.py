from jst.cmd.excute import CommandLine


import sys



cmd = CommandLine()
init = cmd.start()
cmd.new_command("init", "Init command to initialize new repository.")
cmd.new_command("add", "add new files, changes to existing repository.")

def main(argv=sys.argv[1:]):
    args = init.parse_args(argv)
    cmd.echo(args)
    # print(args)