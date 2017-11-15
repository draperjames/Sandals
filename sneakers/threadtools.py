import threading
from . import globalimports as _g

class repeat(threading.Thread):
    def __init__(self, interval=1):
        threading.Thread.__init__(self)
        self.interval = interval
        self.stopped = threading.Event()
        _g.events.append(self.stopped)

    def __call__(self, func):
        self.func = func
        self.start()
        return func

    def run(self):
        while not self.stopped.wait(self.interval):
            self.func()

class loop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stopped = threading.Event()
        _g.events.append(self.stopped)

    def __call__(self, func):
        self.func = func
        self.start()
        return func

    def run(self):
        while not self.stopped.isSet():
            self.func()


