# -*- coding: utf-8 -*-


__author__ = "Leonidas S. Barbosa (kirotawa)"
__version__ = 0x01

import gtk
import sys
import urllib
import urllib2


try:
    import pynotify
except:
    print "Need to install pynotify"
    sys.exit()

pynotify.init("pyremotejobs")


try:
    from BeautifulSoup import BeautifulSoup
except:
    print "Need to install BeautifulSoup\
        install python-beautifulsoup"
    sys.exit()

# globals
import re
class info:
    url = "https://weworkremotely.com/" 
    #tag = "python"
    #position = "Programming"
    regex_motor = re.compile(r"[p|P]ython")

def Tracking():

    request = urllib2.Request(info.url)
    response = urllib2.urlopen(request)
    document = response.read()

    soup = BeautifulSoup(document)

    sections= soup.find('section', {'class':'jobs','id':'category-2'})
    lis = sections.findAll('li')
    import pdb;pdb.set_trace()
    jobs = list()
    for li in lis:
        if li.find('span', {'class':'new'}):
            if info.regex_motor.search(li.find('span',{'class':'title'}).text):
                jobs.append({
                    'link':li.find('a').attrs[0][1],
                    'company':li.find('span',{'class':'company'}).text,
                    'title':li.find('span',{'class':'title'}).text,
                    'date':li.find('span',{'class':'date'}).text,
                })
    return jobs


def Notify(message):
    notify = pynotify.Notification(summary="Situação", message=message)
    notify.set_icon_from_pixbuf(gtk.Label().render_icon(gtk.STOCK_INFO, \
        gtk.ICON_SIZE_LARGE_TOOLBAR)) 
    notify.show()


if __name__ == "__main__":
    print Tracking()
