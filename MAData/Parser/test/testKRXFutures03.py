#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 27.

@author: jayjl
'''
import urllib2
import json
from Parser.models import FuturesData, FuturesInfo, FuturesInvestor
from Parser.util.time.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from Parser.util.time.Date import Date
from Parser.util.time.BusinessDayConvention import BusinessDayConvention
#주체별 선물 거래 데이터 (각 상품군별 데이터 시작날짜 지정 필요, 야간 주간 또한 지정 필요)

calendar = SouthKoreaCalendar.getCalendar(1)

typeCdLists = ['KRDRVFUUSD',
               ]


# typeCdLists = ['KRDRVFUK2I', 'KRDRVFUK2ISP',
#                'KRDRVFUUSD', 'KRDRVFUUSDSP',
#                'KRDRVFUJPY', 'KRDRVFUJPYSP',
#                'KRDRVFUEUR', 'KRDRVFUEURSP',
#                'KRDRVFUBMA', 'KRDRVFUBMASP',
#                'KRDRVFUBM3', 'KRDRVFUBM3SP',
#                'KRDRVFUCNH', 'KRDRVFUCNHSP',
#                'KRDRVFUKGD', 'KRDRVFUKGDSP'
#야간                                    'KRDRVFUK2I', 'KRDRVFUUSD'
#                ]


startDtLists = ['20141208',]
# startDtLists = ['20050311', '20051209',
#                '20050315', '20070827',
#                '20060526', '20070827',
#                '20060526', '20070827',
#                '20101025', '20101025',
#                '20101025', '20101222',
#                '20151005', '20151005',
#                '20151123', '20151123'     
#야간                                    '20091116', '20141208'
#                 ]

endDate = calendar.adjustDate(Date.valueOf('20160325'),
                              BusinessDayConvention.FOLLOWING)

for idx in range(0,len(typeCdLists)):

    isucdStr = typeCdLists[idx]
    
    startDate = calendar.adjustDate(Date.valueOf(startDtLists[idx]),
                                    BusinessDayConvention.FOLLOWING)
    
    processDate = startDate
    
    while processDate.diff(endDate) <= 0 :
        
        fromdtStr = processDate.getDt()
        todtStr = processDate.getDt()
        startDtStr = '20160328'
        #prtTypeStr = 'V' #'V' D:거래량, V:거래대금
        juyaStr = '1' #주간0/야간1/전체on
        
        codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1004%2F10040301%2Fmkd10040301_01&name=form"
        codeR = urllib2.Request(codeAddressStr)
        codeU = urllib2.urlopen(codeR)
        codeStr = codeU.read()
        
        #for volume
        address1 = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
            'isu_cd=' + isucdStr +\
            '&prt_type=' + 'D' +\
            '&juya=' + juyaStr +\
            '&fr_work_dt=' + fromdtStr +\
            '&to_work_dt=' + todtStr +\
            '&strNowDt=' + startDtStr +\
            '&code=' + codeStr
        
        #for amount
        address2 = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
            'isu_cd=' + isucdStr +\
            '&prt_type=' + 'V' +\
            '&juya=' + juyaStr +\
            '&fr_work_dt=' + fromdtStr +\
            '&to_work_dt=' + todtStr +\
            '&strNowDt=' + startDtStr +\
            '&code=' + codeStr
        
        print address1
        print address2
        
        r1 = urllib2.Request(address1)
        r2 = urllib2.Request(address2)
        u1 = urllib2.urlopen(r1)
        u2 = urllib2.urlopen(r2)
        response1 = u1.read()
        response2 = u2.read()
        
        #print response1
        #print response2
        
        result1 = json.loads(response1)['result']
        result2 = json.loads(response2)['result']
        lenResult = len(result1)
        
        for idx in range(0, lenResult) :
            x = result1[idx]
            x2 = result2[idx]
            
            #INVESTOR_CD
            gubunStr = x['gubun']
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
            elif gubunStr.encode('utf-8') == '합계' :
                continue
            
            #OVERNIGHT_CD
            overnightCdStr ='N'
            if juyaStr == '1' :
                overnightCdStr = 'Y' 
            
            #매수 거래량
            buyvolumeStr = x['ms_sum'].replace(',','')
            #매수 거래대금
            buyamountStr = x2['ms_sum'].replace(',','')
            #매도 거래량
            sellvoulmeStr = x['md_sum'].replace(',','')
            sellamountStr = x2['md_sum'].replace(',','')
            
            #매도 비중
            mdrtStr = x['md_rt']    
            #합계
            totStr = x['tot'].replace(',','')
            #매수 비중
            msrtStr = x['ms_rt']
            #합계비중
            totrtStr = x['tot_rt']
            #순매수
            ssumStr = x['s_sum'].replace(',','')
            
            print fromdtStr, isucdStr, gubunStr, codeStr, overnightCdStr, buyvolumeStr, buyamountStr, sellvoulmeStr, sellamountStr
            
            resultDic = {}
            resultDic['dt'] = processDate.getDt()
            resultDic['ticker'] = isucdStr
            resultDic['overnight_cd'] = overnightCdStr
            resultDic['investor_cd'] = codeStr
            resultDic['buy_amount'] = buyamountStr
            resultDic['buy_volume'] = buyvolumeStr
            resultDic['sell_amount'] = sellamountStr
            resultDic['sell_volume'] = sellvoulmeStr
                        
            p = FuturesInvestor(**resultDic)
            
            p.save()
    
        processDate = calendar.adjustDate(processDate.plusDays(1),
                                          BusinessDayConvention.FOLLOWING)
