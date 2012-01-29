# -*- coding:utf-8 -*-

import sys
import urllib
import urllib2

try:
    from BeautifulSoup import BeautifulSoup
except:
    print "É necessário que o BeautifulSoup esteja instalado. \n How to: apt-get \
        install python-beautifulsoup"

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
                print "Sua encomenda ainda não está disponível para tracking no Brasil."

        output += "\n" 
    print output


if __name__ == "__main__":
    if len(sys.argv) == 2:
        Tracking(sys.argv[1])
    else:
        print "Uso: python  BrMailTracking.py codigo_de_rastreio"
