#!/usr/bin/python

import gtk
import sys
import time
from pyremotesjob import handle_to_text

try:
    import pynotify
except:
    print "Need to install pynotify"
    sys.exit()

pynotify.init("pyremotejobs")


def Notify(message="hello"):
    if message:
        notify = pynotify.Notification(summary="New Jobs", message=message)
        notify.set_icon_from_pixbuf(gtk.Label().render_icon(gtk.STOCK_INFO,
                                    gtk.ICON_SIZE_LARGE_TOOLBAR))
        notify.show()

if __name__ == "__main__":
    while(True):
        Notify(handle_to_text())
        time.sleep(60*5)
