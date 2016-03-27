#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 27.

@author: jayjl
'''
import urllib2
import json
from Parser.models import FuturesData, FuturesInfo

dataLists = FuturesData.objects.filter(dt__gte = '20160301').filter(ticker ='KR4101L30006')

for dta in dataLists :
    #print dta.dt, dta.ticker, dta.overnight_cd
    infoList = FuturesInfo.objects.filter(ticker = dta.ticker)
    
    isucdStr = infoList[0]['type_cd']
    fromdtStr = '20160325'
    todtStr = '20160325'
    startDtStr = '20160226'
    #prtTypeStr = 'V' #'V' D:거래량, V:거래대금
    juyaStr = '0' #주간0/야간1/전체on
    if dta.overnight_cd.encode('utf-8') == 'Y' :
        juyaStr = '1'
    
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
    
    #print address1, address2
    
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
            break
        
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
    
