#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 9.

@author: jayjl
'''
import urllib2
import json
from Parser.models import StockInfo


#KRX 신규상장 주식 검색
datasourceStr = 'KRX'
countryStr = 'KR'
ccyCdStr = 'KRW'

codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0406%2F04060401%2Fmkd04060401_01&name=form'
codeR = urllib2.Request(codeAddress)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()

fromdateStr = '20150408'
todateStr = '20160408'
marketgubunStr = 'ALL'
bndlsttypStr = '1' # 1 : 신규상장, 2: 재상장

address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
    '?market_gubun=' + marketgubunStr +\
    '&bnd_lst_typ=' + bndlsttypStr +\
    '&fromdate=' + fromdateStr +\
    '&todate=' + todateStr +\
    '&code=' + codeStr
    
r = urllib2.Request(address)    
u = urllib2.urlopen(r)
response = u.read()
result = json.loads(response)['block1']

for x in result :
    isucdStr = x['isu_cd']
    
    searchCodeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_stkisu&name=form'
    codeR = urllib2.Request(searchCodeAddress)
    codeU = urllib2.urlopen(codeR)
    codeStr = codeU.read()

    searchAddress = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
        '?no=P1' +\
        '&mktsel=ALL' +\
        '&searchText=' + isucdStr +\
        '&code=' + codeStr
    
    searchR = urllib2.Request(searchAddress)
    searchU = urllib2.urlopen(searchR)
    searchResponse = searchU.read()
    searchResult = json.loads(searchResponse)['block1']
    
    tickerStr = searchResult[0]['full_code']
    shortTickerStr = searchResult[0]['short_code']
    nameStr = searchResult[0]['codeName']
    marketNameStr = searchResult[0]['marketName']
    
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
    #p.save()
    
    
    