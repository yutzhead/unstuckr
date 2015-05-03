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
        elif event.keyval == 43:
            position = self.get_position()
            size = self.get_size()
            self.resize(size[0]+2, size[1]+2)
            self.move(position[0]-1, position[1]-1)
        elif event.keyval == 45:
            position = self.get_position()
            size = self.get_size()
            self.resize(size[0]-2, size[1]-2)
            self.move(position[0]+1, position[1]+1)
        elif event.keyval == 65362:
            position = self.get_position()
            self.move(position[0], position[1]-1)
        elif event.keyval == 65364:
            position = self.get_position()
            self.move(position[0], position[1]+1)
        elif event.keyval == 65361:
            position = self.get_position()
            self.move(position[0]-1, position[1])
        elif event.keyval == 65363:
            position = self.get_position()
            self.move(position[0]+1, position[1])
        elif event.keyval == 115:
            self.colors = [self.proto_colors['red'], self.proto_colors['green'], self.proto_colors['blue']]

    def _changeColor(self):
        if self.c < len(self.colors)-1:
            self.c = self.c + 1
        else:
            self.c = 0
        self.override_background_color(Gtk.StateType.NORMAL, self.colors[self.c])

    def fixPixels(self):
        while True:
            GLib.idle_add(self._changeColor)
            time.sleep(1.0/59.91)

    def __init__(self, x, y, size, color):
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

        self.proto_colors = {
            'red': Gdk.RGBA(1.0, 0.0, 0.0, 1.0),
            'green': Gdk.RGBA(0.0, 1.0, 0.0, 1.0),
            'blue': Gdk.RGBA(0.0, 0.0, 1.0, 1.0),
            'white': Gdk.RGBA(1.0, 1.0, 1.0, 1.0),
            'black': Gdk.RGBA(0.0, 0.0, 0.0, 1.0)
        }
        if color == 'sequence':
            self.colors = [self.proto_colors['red'], self.proto_colors['green'], self.proto_colors['blue']]
        else:
            self.colors = [self.proto_colors[color], self.proto_colors['black']]
        self.c = 0

        self.thread = threading.Thread(target=self.fixPixels)
        self.thread.daemon = True
        self.thread.start()


test1 = len(sys.argv) < 3 or (not sys.argv[1].isdigit() or not sys.argv[2].isdigit())
test2 = len(sys.argv) > 4 and (not sys.argv[4] in ['red', 'green', 'blue', 'white', 'sequence'])
if False: #test1 or test2:
    sys.exit('Usage: %s <x> <y> [<rectangle size>] [<color>]\nColors: red, green, blue, white, sequence' % sys.argv[0])

GObject.threads_init()

MainWindow(
    sys.argv[1] if len(sys.argv) > 1 else 50,
    sys.argv[2] if len(sys.argv) > 2 else 50,
    sys.argv[3] if len(sys.argv) > 3 else 25,
    sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] in ['red', 'green', 'blue', 'white', 'sequence'] else 'black'
).show_all()

signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
