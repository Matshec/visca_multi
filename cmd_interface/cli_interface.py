from macros_holder import MacrosHolder


class CliHandler:

    def __init__(self):
        self._macros_holder = MacrosHolder()

    def print_help(self):
        print("to exit enter done,"
          "to register macro enter define and then macro name followed by set on commands separated by commas,"
          "to run macro enter do and then macro name,"
          "to run sigle command enter it's name")

    def identify_input(self, data:str):
        if data.startswith("define"):
            self._macros_holder.register_macro(data[len("define"):])
        elif data.startswith("help"):
            self.print_help()
        elif data.startswith("do"):
            pass
            # run macro
        else:
           print(self._macros_holder._macros)


if __name__ == '__main__':
    cli = CliHandler()
    while True:
        cli_input = input()
        if cli_input == "done":
            break
        cli.identify_input(cli_input)

