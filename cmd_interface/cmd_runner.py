import time
from ..core.visca_lib import D100

class CmdRunner:

    def __init__(self):
        self._main_cam = None
        self._cmds = None

    def setup_interface(self, inf="COM1"):
        self._main_cam = D100(output=inf)
        self._main_cam.init()
        # register functions
        self._cmds = {
            "home": self._main_cam.home,
            "left": self._main_cam.left,
            "right": self._main_cam.right,
            "focus_near": self._main_cam.focus_near,
            "reset_cam": self._main_cam.reset,
            "stop": self._main_cam.stop,
            "up": self._main_cam.up,
            "down": self._main_cam.up,
            "exposure_auto": self._main_cam.exposure_full_auto,
            "wait": time.sleep

        }

    def setup_mock(self, int):
        self._cmds = {
            "home": lambda: print("home"),
            "left": lambda x: print("left %s" % x),
            "wait":  time.sleep
        }

    def available_commands(self):
        return list(self._cmds.keys())

    def parse_and_run(self, data):
        cmd, args = self._parse_to_cmd_and_args(data)
        if args:
            self._cmds[cmd](*args)
        else:
            self._cmds[cmd]()

    def run_macro(self, macro):
        for cmd in macro:
            self.parse_and_run(cmd)

    def _parse_to_cmd_and_args(self, data:str):
        args = None
        data = data.split()
        assert data,  "bad command"
        cmd = str(data[0]).strip()
        if len(data) > 1:
            args = list(map(lambda x: int(x), data[1:]))
        return cmd, args



