from cmd_interface.macros_holder import MacrosHolder
from cmd_interface.cmd_runner import CmdRunner
import sys


class CliHandler:

    def __init__(self):
        self._macros_holder = MacrosHolder()
        self._cmd_runner = CmdRunner()
        self._cmd_runner.setup_mock('dp')

    def print_help(self):
        print("to exit enter done,"
          "to register macro enter define and then macro name followed by set on commands separated by commas,"
          "to run macro enter do and then macro name,"
          "to run sigle command enter it's name with parameter separeted by spaces")

    def identify_input(self, data:str):
        if data.startswith("define"):
            self._macros_holder.register_macro(data[len("define"):])
        elif data.startswith("help"):
            self.print_help()
        elif data.startswith("do"):
            macro = self._macros_holder.get_macro(data[len("do"):])
            print(self._cmd_runner.run_macro(macro))
        elif data.startswith("commands"):
            print(*self._cmd_runner.available_commands())
        else:
            print(self._cmd_runner.parse_and_run(data))


if __name__ == '__main__':
    cli = CliHandler()
    while True:
        try:
            cli_input = input()
            if cli_input == "end":
                break
            cli.identify_input(cli_input)
        except Exception as err:
            print("bad command try again")
