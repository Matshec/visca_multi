
from core.visca_lib import D100


class VariabieIntCam(D100):

    def __init__(self, output="COM1", target_int=1):
        super().__init__(output)
        self.target_int = target_int

    def set_broadcast(self):
        self.target_int = 8

    def set_unicast(self, int):
        self._validate_int(int)
        self.target_int = int

    def set_default(self):
        self.target_int = 1

    def _validate_int(self, num):
        if 8 < num < 1:
            raise ValueError("bad dest given")

    def comm(self, com):
        # 1 is deafult, 2-7 are target intefaces, 8 is broadcast
        self._validate_int(self.target_int)
        body = com[2:]
        header = "8{}".format(self.target_int)
        full_com = header + body
        super().comm(full_com)

