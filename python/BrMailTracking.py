# -*- coding: utf-8 -*-


__author__ = "Leonidas S. Barbosa (kirotawa)"
__version__ = 0.2

import gtk
import sys
import urllib
import urllib2


try:
    import pynotify
except:
    print "É necessário ter o pynotify instalado"
    sys.exit()

pynotify.init("brMailTracking")


try:
    from BeautifulSoup import BeautifulSoup
except:
    print "É necessário que o BeautifulSoup esteja instalado. \n \
           How to: apt-get install python-beautifulsoup"
    sys.exit()


def Tracking(code_tracking):
    url = "http://websro.correios.com.br/sro_bin/txect01$.Inexistente?P_LINGUA=001&P_TIPO=002&P_COD_LIS=%s"

    request = urllib2.Request(url % code_tracking)
    response = urllib2.urlopen(request)
    document = response.read()

    soup = BeautifulSoup(document)

    table = soup.find('table')

    output = ""
    trs = table.findAll('tr')
    for tr in trs:
        tds = tr.findAll('td')
        for td in tds:
            if td.text:
                output += td.text + " "
            else:
                print "Sua encomenda ainda não está disponível para tracking \
                       no Brasil."

        output += "\n"
    if output.replace('\n', '').replace(' ', '') == code_tracking:
        return "O objeto não se encontra disponível para rastreio."
    print output
    return output


def Notify(message):
    notify = pynotify.Notification(summary="Situação", message=message)
    notify.set_icon_from_pixbuf(gtk.Label().render_icon(gtk.STOCK_INFO,
                                gtk.ICON_SIZE_LARGE_TOOLBAR))
    notify.show()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        Notify(Tracking(sys.argv[1]))
    else:
        print "Uso: python  BrMailTracking.py codigo_de_rastreio"
