#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 30.

@author: jayjl
'''
import urllib2
import json
from Parser.models import StockInfo

#주식 주식리스트

codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_stkisu&name=form'

codeR = urllib2.Request(codeAddress)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()

mktselStr = 'KSQ' #KSQ #STK
countryStr = 'KR'
ccyCdStr = 'KRW'
datasourceStr = 'KRX'
address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
    'mktsel=' + mktselStr +\
    '&code=' + codeStr


r = urllib2.Request(address)
    
u = urllib2.urlopen(r)

response = u.read()

#print response

result = json.loads(response)['block1']

for x in result :
    tickerStr = x['full_code']
    shortTickerStr = x['short_code']
    nameStr = x['codeName']
    marketNameStr = x['marketName']
    
    print tickerStr, shortTickerStr, nameStr, marketNameStr
    
    resultDic = {}
    resultDic['ticker'] = tickerStr
    resultDic['name'] = nameStr
    resultDic['short_ticker'] = shortTickerStr
    resultDic['exchange'] = marketNameStr
    resultDic['country'] = countryStr 
    resultDic['ccy_cd'] = ccyCdStr
    resultDic['data_source'] = datasourceStr
    
    p = StockInfo(**resultDic)    
    p.save()
    
    