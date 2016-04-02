#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 2.

@author: jayjl
'''
from Parser.models import StockData, StockInfo, StockInvestor
import urllib2
import json
from Parser.util.time.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from Parser.util.time.Date import Date
from Parser.util.time.BusinessDayConvention import BusinessDayConvention

#주식 투자자별 거래실적

# p, created = StockData.objects.get_or_create(dt ='20160329', 
#                                              ticker = 'KR7095570008')
# 
# 
# if not created : 
#     p.price_open = '123'

tickerLists = StockInfo.objects.filter(data_source = 'KRX').filter(exchange = 'KOSPI')

calendar = SouthKoreaCalendar.getCalendar(1)

startDate = calendar.adjustDate(Date.valueOf('20160102'),
                                    BusinessDayConvention.FOLLOWING)

endDate = calendar.adjustDate(Date.valueOf('20160331'),
                              BusinessDayConvention.FOLLOWING)


for tic in tickerLists :
    
    isuCdStr = tic.ticker            
    periodselectorStr = 'day'

    processDate = startDate
        
    while processDate.diff(endDate) <= 0 :
        
        codeAddressStr = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1002%2F10020101%2Fmkd10020101&name=form'
        codeR = urllib2.Request(codeAddressStr)
        codeU = urllib2.urlopen(codeR)
        codeStr = codeU.read()
           
        fromdateStr = processDate.getDt()
        todate = processDate.getDt()
        
        address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
            '?isu_cd=' + isuCdStr +\
            '&period_selector=' + periodselectorStr +\
            '&fromdate=' + fromdateStr +\
            '&todate=' + todate +\
            '&code=' + codeStr
            
        print address
            
        r = urllib2.Request(address)
            
        u = urllib2.urlopen(r)
        
        response = u.read()
        
        
        result = json.loads(response)['block1']
        
        for x in result :
            gubunStr = x['invst_nm']
            codeStr = ''        
            if gubunStr.encode('utf-8') == '금융투자' :
                codeStr = 'INST'
            elif gubunStr.encode('utf-8') == '보험' :
                codeStr = 'INSU'
            elif gubunStr.encode('utf-8') == '집합투자' :
                codeStr = 'COLL'
            elif gubunStr.encode('utf-8') == '은행' :
                codeStr = 'BANK'
            elif gubunStr.encode('utf-8') == '기타금융' :
                codeStr = 'ETCI'
            elif gubunStr.encode('utf-8') == '연기금 등' :
                codeStr = 'PENS'
            elif gubunStr.encode('utf-8') == '기타법인' :
                codeStr = 'ETCC'
            elif gubunStr.encode('utf-8') == '개인' :
                codeStr = 'INDI'
            elif gubunStr.encode('utf-8') == '외국인' :
                codeStr = 'FORE'
            elif gubunStr.encode('utf-8') == '기타외국인' :
                codeStr = 'ETCF'
            elif gubunStr.encode('utf-8') == '국가.지자체' :
                codeStr = 'GOVE'
            elif gubunStr.encode('utf-8') == '연기금' :
                codeStr = 'PENS'
            elif gubunStr.encode('utf-8') == '사모' :
                codeStr = 'FUND'
            elif gubunStr.encode('utf-8') == '투신' :
                codeStr = 'TRUS'        
            elif gubunStr.encode('utf-8') == '합계' :
                continue
            elif gubunStr.encode('utf-8') == '기관합계' :
                continue
            
            #매수거래량
            buyvolumeStr = x['bidvol'].replace(',','')
            x['bidvol_rt']
            #매도거래량
            sellvolumeStr = x['askvol'].replace(',','')
            x['askvol_rt']    
            x['netaskvol']
            
            #매수거래대금
            buyamountStr = x['bidval'].replace(',','')
            x['bidval_rt']
            
            #매도거래대금
            sellamountStr = x['askval'].replace(',','')
            x['askval_rt']
            x['netaskval']
            
            print isuCdStr, processDate.getDt(), codeStr, buyvolumeStr, sellvolumeStr, buyamountStr, sellamountStr
            
            resultDic = {}
            resultDic['dt'] = processDate.getDt()
            resultDic['ticker'] = isuCdStr
            resultDic['investor_cd'] = codeStr
            resultDic['buy_amount'] = buyamountStr
            resultDic['buy_volume'] = buyvolumeStr
            resultDic['sell_amount'] = sellamountStr
            resultDic['sell_volume'] = sellvolumeStr
             
            p = StockInvestor(**resultDic)
            p.save()
            
    
        processDate = calendar.adjustDate(processDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
