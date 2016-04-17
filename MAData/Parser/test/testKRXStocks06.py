#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 9.

@author: jayjl
'''
import urllib2
import json
from Parser.models import StockInfo

#KRX 상장페지 주식


codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0406%2F04060600%2Fmkd04060600&name=form'
codeR = urllib2.Request(codeAddress)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()

fromdateStr = '20160408'
todateStr = '20160408'

address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
    '?market_gubun=ALL' +\
    '&fromdate=' + fromdateStr +\
    '&todate=' + todateStr +\
    '&code=' + codeStr
    
r = urllib2.Request(address)    
u = urllib2.urlopen(r)
response = u.read()
result = json.loads(response)['block1']

for x in result :
    isucdStr = x['isu_cd']
    
    list = StockInfo.objects.filter(short_ticker = isucdStr)
    
    #TODO


