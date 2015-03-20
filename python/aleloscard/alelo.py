# -*- coding: utf-8 -*-

# Author: Leonidas S. Barbosa aka Kirotawa
# E-mail: kirotawa[put a sign here]gmail(dot)com

import sys
import urllib
import urllib2


try:
    from BeautifulSoup import BeautifulSoup
except:
    print 'You should install BeautifulSoup module'
    sys.exit()

# Conf: put your cards numbers here.
cards = {'ref': '0000000000000000', 'ali': '0000000000000'}

# Url crawled.
url = "https://www.cartoesbeneficio.com.br/inst/convivencia/SaldoExtrato.jsp"

try:
    values = {'numeroCartao': cards['ref'], 'primeiroAcesso': 'S',
              'origem': 'Alelo'}
except:
    print 'Use: alelo ref or alelo ali'
    sys.exit()

data = urllib.urlencode(values)
request = urllib2.Request(url, data)

response = urllib2.urlopen(request)
document = response.read()
soup = BeautifulSoup(document)

print 'Seu saldo é:  %s' % str(soup.findAll('table')[-1].
      findAll('td')[1].next)
