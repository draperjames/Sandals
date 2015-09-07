from .tkimports import *
from . import globalimports as _g


class slot(tkinter.Frame):
    def __init__(self, **kw):
        self.kw = kw

    def __enter__(self):
        self._root_old = _g.root
        self._pack_side_old = _g.pack_side
        tkinter.Frame.__init__(self, self._root_old, **self.kw)
        self.pack( side=self._pack_side_old, fill=tkinter.X)
        _g.root = self

    def __exit__(self, type, value, traceback):
        _g.root = self._root_old
        _g.pack_side = self._pack_side_old

class stack(slot):
    def __init__(self, **kw):
        slot.__init__(self, **kw)
    def __enter__(self):
        global _pack_side
        slot.__enter__(self)
        _g.pack_side = TOP
        return _g.root

class flow(slot):
    def __init__(self, **kw):
        slot.__init__(self, **kw)
    def __enter__(self):
        slot.__enter__(self)
        _g.pack_side = LEFT
        return _g.root
