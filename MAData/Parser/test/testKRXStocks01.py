#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 30.

@author: jayjl
'''
import urllib2
import json

codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_stkisu&name=form'

codeR = urllib2.Request(codeAddress)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()

mktselStr = 'STK' #KSQ

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
    
    