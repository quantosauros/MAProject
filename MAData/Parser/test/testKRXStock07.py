#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 15.

@author: jayjl
'''
import urllib2
import json
from Parser.models import StockSuspension
import datetime

#주식 거래정지 목록

codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0403%2F04030300%2Fmkd04030300&name=form'
codeR = urllib2.Request(codeAddress)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()


address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' + \
    '?gubun=ALL' + \
    '&code=' + codeStr
    
r = urllib2.Request(address)    
u = urllib2.urlopen(r)
response = u.read()
result = json.loads(response)['block1']

now = datetime.datetime.now()
today = now.strftime('%Y%m%d') 

print today

for x in result : 
    isusrtcdStr = x['isu_srt_cd']
    trstpdtStr = x['tr_stp_dt'].replace('/', '')
    trstprsntypStr = x['tr_stp_rsn_typ']
    
    searchCodeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_stkisu&name=form'
    codeR = urllib2.Request(searchCodeAddress)
    codeU = urllib2.urlopen(codeR)
    codeStr = codeU.read()

    searchAddress = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
        '?no=P1' +\
        '&mktsel=ALL' +\
        '&searchText=' + isusrtcdStr +\
        '&code=' + codeStr
    
    searchR = urllib2.Request(searchAddress)
    searchU = urllib2.urlopen(searchR)
    searchResponse = searchU.read()
    searchResult = json.loads(searchResponse)['block1']
    
    tickerStr = searchResult[0]['full_code']
    shortTickerStr = searchResult[0]['short_code']
    nameStr = searchResult[0]['codeName']
    marketNameStr = searchResult[0]['marketName']
    
    print tickerStr, nameStr, marketNameStr, trstpdtStr, trstprsntypStr
    
    resultDic = {}
    resultDic['dt'] = today
    resultDic['ticker'] = tickerStr
    resultDic['start_dt'] = trstpdtStr
    resultDic['reason'] = trstprsntypStr
        
    p = StockSuspension(**resultDic)
    
    p.save()
    