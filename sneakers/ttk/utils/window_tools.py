# -*- coding: utf-8 -*-
from tkinter import Tk


def set_geometry(self, width=None, height=None, x=None, y=None):
    width = width or 1
    height = height or 1
    y = y or 0
    x = x or 0
    window_size = "{:d}x{:d}".format(int(width), int(height))
    window_size = '+'.join([window_size, str(int(x)), str(int(y))])
    self.geometry(window_size)


setattr(Tk, 'set_geometry', set_geometry)


def relative_position(self, width=500, height=200):
    width = int(width)
    height = int(height)
    # Width of the screen.
    screen_width = self.winfo_screenwidth()
    # Height of the screen.
    screen_height = self.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    self.set_geometry(width, height, x, y)


setattr(Tk, 'relative_position', relative_position)


# if __name__ == '__main__':
#     root = Tk()
#     root.title("Test")
#     # root.set_geometry(width=80, height=80)
#     root.relative_position(500, 800)
#     root.config()
#
#     root.mainloop()
