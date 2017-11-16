from .ttkimports import *
from . import globalimports as _g
from contextlib import contextmanager


class button(Button, object):
    def __init__(self, text="", **kw):
        self.kw   = kw
        self.textvariable = StringVar()
        self.textvariable.set(self.kw['text'] if 'text' in self.kw else text)
        if 'text' in self.kw:
            del self.kw['text']
        Button.__init__(self, _g.root, textvariable = self.textvariable, **kw)
        self.pack( side = _g.pack_side )

    def __call__(self, func):
        func.button = self
        self.config(command = lambda: func())
        return func

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

class label(Label, object):
    def __init__(self, text="", **kw):
        self.kw   = kw
        self.textvariable = StringVar()
        self.textvariable.set(self.kw['text'] if 'text' in self.kw else text)
        if 'text' in self.kw:
            del self.kw['text']
        Label.__init__(self, _g.root, textvariable=self.textvariable, **kw)
        self.pack( side=_g.pack_side )

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

class message(Message, object):
    def __init__(self, text="", **kw):
        self.kw = kw
        self.textvariable = StringVar()
        self.textvariable.set(self.kw['text'] if 'text' in self.kw else text)
        if 'text' in self.kw:
            del self.kw['text']
        Message.__init__(self, _g.root, textvariable=self.textvariable, anchor=NW, **kw)
        self.pack( side=_g.pack_side )

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

class editBox(Entry, object):
    def __init__(self, text="", *args, **kwargs):
        self.textvariable = StringVar()
        self.textvariable.set(text)
        Entry.__init__(self, _g.root, textvariable=self.textvariable, **kwargs)
        self.pack(side=_g.pack_side)

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

def showInfo(title = "Info", message = "", **kw):
    messagebox.showinfo(title, message, **kw)

def showWarning(title = "Warning", message = "", **kw):
    messagebox.showwarning(title, message, **kw)

def showError(title = "Error", message = "", **kw):
    messagebox.showerror(title, message, **kw)

def askYesNo(title = "Question", message = "", **kw):
    return messagebox.askyesno(title, message, **kw)

def askOkCancel(title = "Question", message = "", **kw):
    return messagebox.askokcancel(title, message, **kw)

def askRetryCancel(title = "Retry?", message = "", **kw):
    return messagebox.askretrycancel(title, message, **kw)

def askYesNoCancel(title = "Retry?", message = "", **kw): # returns None on cancel
    return messagebox.askyesnocancel(title, message, **kw)

def askOpenFilename(**kw):
    return filedialog.askopenfilename(**kw)

def askSaveAsFilename(**kw):
    return filedialog.asksaveasfilename(**kw)

def askOpenFilenames(**kw):
    return filedialog.askopenfilenames(**kw)

@contextmanager
def askOpenFile(**kw):
    file = filedialog.askopenfile(**kw)
    try:
        yield file
    finally:
        file.close()

@contextmanager
def askOpenFiles(**kw):
    files = filedialog.askopenfiles(**kw)
    try:
        yield files
    finally:
        for file in files:
            file.close()

@contextmanager
def askSaveAsFile(**kw):
    file = filedialog.asksaveasfile(**kw)
    try:
        yield file
    finally:
        file.close()

def askDirectory(**kw):
    return filedialog.askdirectory(**kw)

def askInteger(title, prompt, **kw):
    return simpledialog.askinteger(title, prompt, **kw)

def askFloat(title, prompt, **kw):
    return simpledialog.askfloat(title, prompt, **kw)

def askString(title, prompt, **kw):
    return simpledialog.askstring(title, prompt, **kw)

class scrolledText(scrolledtext.ScrolledText, object):
    def __init__(self, text = "", bg='white', height=10, expand=True, editable=True, **kw):
        scrolledtext.ScrolledText.__init__(self, _g.root, bg=bg, height=height, **kw)
        self.insert(END, text)
        if not editable:
            self.config(state=DISABLED)
        self.pack(fill=BOTH, side=_g.pack_side, expand=expand)

    @property
    def editable(self):
        return self.state==NORMAL

    @editable.setter
    def editable(self, editable):
        if editable:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)

class checkBox(Checkbutton, object):
    def __init__(self, text="", checked=False, *args, **kwargs):
        self.textvariable = StringVar()
        self.textvariable.set(text)
        self._checked = BooleanVar()
        self._checked.set(checked)
        Checkbutton.__init__(self, _g.root, textvariable=self.textvariable, variable=self._checked, **kwargs)
        self.pack(side=_g.pack_side)

    def __call__(self, func):
        self.config(command = lambda: func(self.checked))
        return func

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

    @property
    def checked(self):
        return self._checked.get()

    @checked.setter
    def checked(self, text):
        self._checked.set(text)


class radioButton(Radiobutton, object):
    def __init__(self, value, text="", variable=None, checked=False, *args, **kwargs):
        self.textvariable = StringVar()
        self.textvariable.set(text)
        if variable is None:
            variable = _g.radioVariable
        self.variable = variable
        Radiobutton.__init__(self, _g.root, textvariable=self.textvariable, variable=self.variable, value=value, **kwargs)
        self.pack(side=_g.pack_side)

    def __call__(self, func):
        self.config(command = lambda: func(self.variable.get()))
        return func

    @property
    def text(self):
        return self.textvariable.get()

    @text.setter
    def text(self, text):
        self.textvariable.set(text)

class radioSet(object):
    def __enter__(self):
        self.IntVar = IntVar()
        _g.radioVariable = self.IntVar
        return self

    def __exit__(self, type, value, traceback):
        pass

    @property
    def number(self):
        return self.IntVar.get()

    @number.setter
    def number(self, n):
        self.IntVar.set(n)

class spinBox(Spinbox, object):
    def __init__(self, **kw):
        Spinbox.__init__(self, _g.root, **kw)
        self.pack(side=_g.pack_side)

    def __call__(self, func):
        self.config(command = lambda: func(self.get()))
        return func

    @property
    def value(self):
        return self.get()

class scaleBar(Scale, object):
    def __init__(self, range=None, enabled=True, **kw):
        Scale.__init__(self, _g.root, **kw)
        self.pack(side=_g.pack_side)
        self._enabled = enabled

    def __call__(self, func):
        self.config(command = func)
        return func

    @property
    def value(self):
        return self.get()

    @value.setter
    def value(self, value):
        if not self.enabled:
            self.config(state=NORMAL)
        self.set(value)
        if not self.enabled:
            self.config(state=DISABLED)

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        self._enabled = enabled
        if enabled:
            self.config(state=NORMAL)
        else:
            self.config(state=DISABLED)

class optionMenu(OptionMenu, object):
    def __init__(self, *values, **kw):
        self.values = values
        self.kw = kw
        self.StringVar = StringVar()
        OptionMenu.__init__(self, _g.root, self.StringVar, *values, **kw)
        self.pack(side=_g.pack_side)

    def __call__(self, func):
        self.StringVar = StringVar()
        OptionMenu.__init__(self, _g.root, self.StringVar, *self.values, command = func, **self.kw)
        self.pack(side=_g.pack_side)
        return func

    @property
    def option(self):
        return self.StringVar.get()

    @option.setter
    def option(self, option):
        self.StringVar.set(option)

class listBox(Listbox, object):
    def __init__(self, **kw):
        values = kw['values']
        if 'values' in kw:
            del kw['values']
        Listbox.__init__(self, _g.root, **kw)
        self.pack(side=_g.pack_side)
        for item in values:
            self.insert(END, item)

    @property
    def selection(self):
        return self.curselection()[0]
