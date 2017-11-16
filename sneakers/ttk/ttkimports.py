# -*- coding: utf-8 -*-

# Python 3
try:
    # ttk imports
    from tkinter.ttk import Button
    from tkinter.ttk import Checkbutton
    from tkinter.ttk import Entry
    from tkinter.ttk import Label
    from tkinter.ttk import OptionMenu
    from tkinter.ttk import Radiobutton
    from tkinter.ttk import Scale
    # from tkinter.ttk import Frame
    # from tkinter.ttk import Scrollbar

    # regular tkinter imports.
    # from tkinter import Tk
    from .utils.window_tools import Tk

    from tkinter import Frame
    from tkinter import Scrollbar

    from tkinter import Canvas
    from tkinter import Listbox
    from tkinter import Message
    from tkinter import Spinbox
    from tkinter import IntVar
    from tkinter import StringVar
    from tkinter import BooleanVar
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import simpledialog
    from tkinter import scrolledtext
    from tkinter import N
    from tkinter import NE
    from tkinter import E
    from tkinter import SE
    from tkinter import S
    from tkinter import SW
    from tkinter import W
    from tkinter import NW
    from tkinter import X
    from tkinter import CENTER
    from tkinter import BOTTOM
    from tkinter import LEFT
    from tkinter import RIGHT
    from tkinter import TOP
    from tkinter import NONE
    from tkinter import END
    from tkinter import BOTH
    from tkinter import NORMAL
    from tkinter import ACTIVE
    from tkinter import DISABLED
    from tkinter import FLAT
    from tkinter import RAISED
    from tkinter import SUNKEN
    from tkinter import GROOVE
    from tkinter import RIDGE
    from tkinter import TRUE
    from tkinter import FALSE

# Python 2
except ImportError:
    print("sneakers.ttk is currently not supported for Python 2.7")
    # import Tkinter as tkinter
    # import tkMessageBox as messagebox
    # import tkFileDialog as filedialog
    # import tkSimpleDialog as simpledialog
    # import ScrolledText as scrolledtext
    # from Tkinter import Scrollbar
    #
    # from Tkinter import N
    # from Tkinter import NE
    # from Tkinter import E
    # from Tkinter import SE
    # from Tkinter import S
    # from Tkinter import SW
    # from Tkinter import W
    # from Tkinter import NW
    #
    # from Tkinter import CENTER
    # from Tkinter import BOTTOM
    # from Tkinter import LEFT
    # from Tkinter import RIGHT
    # from Tkinter import TOP
    # from Tkinter import NONE
    #
    # from Tkinter import NORMAL
    # from Tkinter import ACTIVE
    # from Tkinter import DISABLED
    #
    # from Tkinter import FLAT
    # from Tkinter import RAISED
    # from Tkinter import SUNKEN
    # from Tkinter import GROOVE
    # from Tkinter import RIDGE
    #
    # from Tkinter import TRUE
    # from Tkinter import FALSE
