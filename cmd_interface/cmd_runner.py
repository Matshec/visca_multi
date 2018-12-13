import time
#from core.visca_lib import D100
from core.var_int_visca import VariabieIntCam

class CmdRunner:

    def __init__(self):
        self._main_cam = None
        self._cmds = None

    def setup_interface(self, inf="COM3"):
        self._main_cam = VariabieIntCam(output=inf)
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
            "down": self._main_cam.down,
            "exposure_auto": self._main_cam.exposure_full_auto,
            "wait": time.sleep,
            "unicast": self._main_cam.set_unicast,
            "multicast": self._main_cam.set_broadcast,
            "set_def": self._main_cam.set_default,
            "addr": self._main_cam.dupa
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
        response = "response"
        cmd, args = self._parse_to_cmd_and_args(data)
        func = self._cmds[cmd]
        if args:
            func(*args)
        else:
            func()
        #check if call read on channel
        if "set" not in func.__name__ and isinstance(func.__self__, VariabieIntCam):
            print( 'jestem grzecznym ifem' )
            response = self._main_cam.read()
        return response


    def run_macro(self, macro):
        response = ""
        for cmd in macro:
            print(cmd)
            res = self.parse_and_run(cmd)
            response += res
        return response

    def _parse_to_cmd_and_args(self, data:str):
        args = None
        data = data.split()
        assert data,  "bad command"
        cmd = str(data[0]).strip()
        if len(data) > 1:
            args = list(map(lambda x: int(x), data[1:]))
        return cmd, args



