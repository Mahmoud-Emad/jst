from jst.cmd.excute import CommandLine
import sys



cmd = CommandLine()
init = cmd.init()
cmd.new_command("init", "Init command to initialize new repository.")

def main(argv=sys.argv[1:]):
    args = init.parse_args(argv)
    print(cmd)
    cmd.echo(args)
    # print(args)