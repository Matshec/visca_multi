

class MacrosHolder:

    def __init__(self):
        self._macros = {}

    def register_macro(self, macro_data):
        """
        register macro in dictionary with key as name and body as list of commands with parameters
        :param macro_data: string with macro name and commands
        """
        strip = macro_data.lstrip()
        macro_name_indenx = strip.find(' ')
        macro_name = strip[:macro_name_indenx]
        splitted = strip[macro_name_indenx:].split(',')
        macro_body = map(lambda x: x.lstrip(), splitted)
        self._macros[macro_name] = list(macro_body)

    def get_macro(self, name):
        name = name.strip()
        return self._macros.get(name)

