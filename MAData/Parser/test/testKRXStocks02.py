#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 30.

@author: jayjl
'''
import urllib2
import json

codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0402%2F04020100%2Fmkd04020100t3_02&name=chart"
codeR = urllib2.Request(codeAddressStr)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()

fromdateStr = '20160322'
todateStr = '20160329'
dategubunStr = '2' #1 : 실시간, 2: 일별, 3:월별

address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
    '&isu_cd=' + 'KR7005930003' +\
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
    dtStr = x['trd_dd']
    closePriceStr = x['tdd_clsprc']
    updownStr = x['fluc_tp']
    diffStr = x['tdd_cmpr']
    volumeStr = x['acc_trdvol']
    amountStr = x['acc_trdval']
    openPriceStr = x['tdd_opnprc']
    highPriceStr = x['tdd_hgprc']
    lowPriceStr = x['tdd_lwprc']
    marketCapStr = x['mktcap']
    listedShareStr = x['list_shrs']
    
    print dtStr, closePriceStr, updownStr, diffStr, volumeStr, amountStr, openPriceStr,highPriceStr,lowPriceStr,marketCapStr, listedShareStr
    
    



