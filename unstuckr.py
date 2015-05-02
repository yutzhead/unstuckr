#!/usr/bin/python3
from gi.repository import Gtk, GLib, GObject, Gdk
import signal
import random
import threading
import time
import sys
import math

class MainWindow(Gtk.Window):
    def _keyPress(self, widget, event):
        if Gdk.keyval_name(event.keyval) == 'Escape':
            Gtk.main_quit()

    def _changeColor(self):
        self.override_background_color(Gtk.StateType.NORMAL, self.colors[self.color])

        if self.color == 3: self.color = 0
        else: self.color = self.color+1

    def fixPixels(self):
        while True:
            GLib.idle_add(self._changeColor)
            time.sleep(1.0/59.91)

    def __init__(self, x, y, size):
        Gtk.Window.__init__(self)
        self.connect('key-press-event', self._keyPress)
        self.connect("delete-event", Gtk.main_quit)


        size = float(size)
        x = float(x)
        y = float(y)

        self.resize(size, size)
        self.move(math.ceil(x-(size/2)), math.ceil(y-(size/2)))


        self.set_decorated(False)
        self.set_keep_above(True)

        self.colors = [
            Gdk.RGBA(1.0, 0.0, 0.0, 1.0),
            Gdk.RGBA(0.0, 1.0, 0.0, 1.0),
            Gdk.RGBA(0.0, 0.0, 1.0, 1.0),
            Gdk.RGBA(1.0, 1.0, 1.0, 1.0),
        ]
        self.color = 0

        self.thread = threading.Thread(target=self.fixPixels)
        self.thread.daemon = True
        self.thread.start()

if len(sys.argv) < 3 or (not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
    sys.exit('Usage: %s <x> <y> [<rectangle size>]' % sys.argv[0])

GObject.threads_init()
m = MainWindow(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 1)
m.show_all()

signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
