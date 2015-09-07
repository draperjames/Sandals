from .tkimports import *
from . import globalimports as _g
from .scrollbar import AutoScrollbar

class window(tkinter.Tk):
    def __init__(self, title="Window", **kw):
        tkinter.Tk.__init__(self)
        self.title(title)
        self.kw = kw

    def __enter__(self):

        # create scroll bar
        self.vscrollbar = AutoScrollbar(self)
        self.vscrollbar.grid(row=0, column=1, sticky=N+S)

        # create canvas
        self.canvas = tkinter.Canvas(self,
                        yscrollcommand=self.vscrollbar.set, bd=5)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        # configure scroll bar for canvas
        self.vscrollbar.config(command=self.canvas.yview)

        # make the canvas expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create frame in canvas
        self.frame = tkinter.Frame(self.canvas)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)


        _g.pack_side = TOP
        _g.root = self.frame
        return self # was _g.root for some reason

    def __exit__(self, type, value, traceback):

        # puts tkinter widget onto canvas
        self.canvas.create_window(0, 0, anchor=NW, window=self.frame, width = int(self.canvas.config()['width'][4])-int(self.vscrollbar.config()['width'][4]))

        # deal with canvas being resized
        def resize_canvas(event):
            self.canvas.create_window(0, 0, anchor=NW, window=self.frame, width = int(event.width)-int(self.vscrollbar.config()['width'][4]))
        self.canvas.bind("<Configure>", resize_canvas)

        # updates geometry management
        self.frame.update_idletasks()

        # set canvas scroll region to all of the canvas
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # set minimum window width
        self.update()
        self.minsize(self.winfo_width(), 0)
        self.config(**self.kw)

        self.frame.update()

        # start mainloop
        self.mainloop()

        # window closed...

        _g.pack_side = None

        # stop all ongoing _g.events
        [event.set() for event in _g.events]
