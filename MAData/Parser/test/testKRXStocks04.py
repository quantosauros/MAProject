#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 2.

@author: jayjl
'''
#주식 - 공매도
import urllib2
import json
from Parser.models import StockShort, StockInfo

tickerLists = StockInfo.objects.filter(data_source = 'KRX').filter(exchange = 'KOSPI')
periodstrtddStr = '20160101'
periodendddStr = '20160331'

for tic in tickerLists : 
    
    codeAddressStr = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1002%2F10020104%2Fmkd10020104&name=form'
    codeR = urllib2.Request(codeAddressStr)
    codeU = urllib2.urlopen(codeR)
    codeStr = codeU.read()
        
    jisuschtypeStr = '1' #1 : 개별종목, 2: 개별지수
    isucdStr = tic.ticker
    
    address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
        '?jisu_sch_type=' + jisuschtypeStr +\
        '&isu_cd=' + isucdStr +\
        '&period_strt_dd=' + periodstrtddStr +\
        '&period_end_dd=' + periodendddStr +\
        '&code=' + codeStr
        
    print address
                
    r = urllib2.Request(address)
        
    u = urllib2.urlopen(r)
    
    response = u.read()
    
    result = json.loads(response)['block1']
    
    for x in result :
        dtStr = x['trd_dd'].replace('/','')
        shortvolumeStr = int(x['srtsell_vol'].replace(',', '')) 
        shortvalueStr = int(x['srtsell_val'].replace(',', '')) * 1000
        totalvolumeStr = int(x['all_vol'].replace(',', '')) * 1000
        totalvalueStr = int(x['all_val'].replace(',', '')) * 1000000
        totalshareStr = int(x['all_shrs'].replace(',', '')) * 1000
        
        print isucdStr, dtStr, shortvolumeStr, shortvalueStr, totalvolumeStr, totalvalueStr, totalshareStr
        
        resultDic = {}
        resultDic['dt'] = dtStr
        resultDic['ticker'] = isucdStr
        resultDic['volume'] = shortvolumeStr
        resultDic['amount'] = shortvalueStr
        resultDic['total_volume'] = totalvolumeStr
        resultDic['total_amount'] = totalvalueStr
        resultDic['total_shares'] = totalshareStr
        
        p = StockShort(**resultDic)
        p.save()
