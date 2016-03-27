#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 24.

@author: jayjl
'''
import urllib2
import json
from Parser.models import FuturesInfo

#국채선물 리스트
yearStr = '2016'
prodIdList = ['KRDRVFUK2I',
'KRDRVFUBM3',
'KRDRVFUBMA',
'KRDRVFUUSD',
'KRDRVFUJPY',
'KRDRVFUEUR',
'KRDRVFUCNH',
'KRDRVFUKGD',
]

codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_fuisu&name=form"
codeR = urllib2.Request(codeAddressStr)
codeU = urllib2.urlopen(codeR)
codeStr = codeU.read()
#codeStr = "0Nf/Z7DN6rqZB3X07SViDOSLAV/b2Wj108z+NiUD+htjPiyAadCyurUeq4QEmVkT5v+GsFUWK4gK32MwmEk0a7OiZr4RJrAKO5yAyJ51rqk="

for prodIdStr in prodIdList :    
    print "================" + prodIdStr + "================"
    address = "http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?schdate=" +\
        yearStr + "&mktsel=" + prodIdStr + "&stockTp=&" + "schIsuCd=" + prodIdStr +\
        "&pagePath=%2Fcontents%2FCOM%2FFinderFuIsu.jsp" +\
        "&code=" + codeStr
    
    r = urllib2.Request(address)
    
    u = urllib2.urlopen(r)
    
    response = u.read()
    
    #print response
    
    result = json.loads(response)['result']
    
    
    for x in result :
        tickerStr = x['isu_cd']
        nameStr = x['isu_nm']
        shortTickerStr = x['shrt_isu_cd'] 
        expireDtStr = x['expmm']
        spreadType = x['spd_tp']
        
        print tickerStr, nameStr, shortTickerStr, expireDtStr, spreadType
        
        resultDic = {}
        resultDic['ticker'] = tickerStr
        resultDic['name'] = nameStr
        resultDic['short_ticker'] = shortTickerStr
        resultDic['expire_dt'] = expireDtStr
        resultDic['spread_type'] = spreadType 
        resultDic['type_cd'] = prodIdStr
        
        p = FuturesInfo(**resultDic)
        
        p.save()
    
    


