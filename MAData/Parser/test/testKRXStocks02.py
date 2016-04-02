#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 30.

@author: jayjl
'''
import urllib2
import json
from Parser.models import StockData, StockInfo

#주식 히스토리 주가 데이터

fromdateStr = '20160101'
todateStr = '20160331'
dategubunStr = '2' #1 : 실시간, 2: 일별, 3:월별

tickerLists = StockInfo.objects.filter(data_source = 'KRX')

for tic in tickerLists : 
    
    isucodeStr = tic.ticker
    isuNameStr = tic.name
    
    codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0402%2F04020100%2Fmkd04020100t3_02&name=chart"
    codeR = urllib2.Request(codeAddressStr)
    codeU = urllib2.urlopen(codeR)
    codeStr = codeU.read()
    
    address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
        '&isu_cd=' + isucodeStr +\
        '&dateGubun=' + dategubunStr +\
        '&fromdate=' + fromdateStr +\
        '&todate=' + todateStr +\
        '&code=' + codeStr
    
    r = urllib2.Request(address)
            
    u = urllib2.urlopen(r)
    
    response = u.read()
    
    print response
        
    result = json.loads(response)['block1']
    
    for x in result : 
        dtStr = x['trd_dd'].replace('/','')
        closePriceStr = x['tdd_clsprc'].replace(',', '')
        updownStr = x['fluc_tp'].replace(',', '')
        diffStr = x['tdd_cmpr'].replace(',', '')
        volumeStr = x['acc_trdvol'].replace(',', '')
        amountStr = x['acc_trdval'].replace(',', '')
        openPriceStr = x['tdd_opnprc'].replace(',', '')
        highPriceStr = x['tdd_hgprc'].replace(',', '')
        lowPriceStr = x['tdd_lwprc'].replace(',', '')
        marketCapStr = x['mktcap'].replace(',', '')
        listedShareStr = x['list_shrs'].replace(',', '')
        
        print isucodeStr, isuNameStr, dtStr, closePriceStr, updownStr, diffStr, volumeStr, amountStr, openPriceStr,highPriceStr,lowPriceStr,marketCapStr, listedShareStr
        
        resultDic = {}
        resultDic['dt'] = dtStr
        resultDic['ticker'] = isucodeStr
        resultDic['price_close'] = closePriceStr
        resultDic['price_open'] = openPriceStr
        resultDic['price_high'] = highPriceStr
        resultDic['price_low'] = lowPriceStr
        resultDic['volume'] = volumeStr
        resultDic['amount'] = amountStr
        resultDic['marketcap'] = marketCapStr
        resultDic['listed_shares'] = listedShareStr
        p, created = StockData.objects.get_or_create(dt = dtStr, ticker = isucodeStr,
                                                     defaults = resultDic) 
        if not created : 
            p.save()
        #p = StockData(**resultDic)
                



