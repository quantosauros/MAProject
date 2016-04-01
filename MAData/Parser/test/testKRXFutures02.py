#-*- coding: utf-8 -*-
'''
Created on 2016. 3. 24.

@author: jayjl
'''
import urllib2
import json
from Parser.models import FuturesData, FuturesInfo
from Parser.util.DataCollector import DataCollector
#선물 히스토리 데이터
fromdateStr = '20000101'
todateStr = '20160327'

#tickerLists = FuturesInfo.objects.filter(expire_dt__gte ='201512').order_by('expire_dt')
tickerLists = FuturesInfo.objects.filter(type_cd__contains = 'KRDRVFUS').order_by('expire_dt')
#tickerLists = FuturesInfo.objects.filter().order_by('expire_dt')

for tic in tickerLists :
    #isucdStr = 'KR4478KCL1S6'
    isucdStr = tic.ticker
    
    codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F06%2F0601%2F06010200%2Fmkd06010200_04&name=chart"
    codeR = urllib2.Request(codeAddressStr)
    codeU = urllib2.urlopen(codeR)
    codeStr = codeU.read()
    
    address = "http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?" +\
        "&isu_cd=" + isucdStr +\
        "&fromdate=" + fromdateStr +\
        "&todate=" + todateStr +\
        "&code=" + codeStr
    print address
    
    r = urllib2.Request(address)
        
    u = urllib2.urlopen(r)
    
    response = u.read()
    
    #print response
    
    result = json.loads(response)['block1']
    
    
    idx = 0
    maxlen = len(result)
    for x in result :         
        dtStr = x['work_dt'].replace('/','')                #일자         
        closePriceStr = x['end_pr_7'].replace(",", "")       #종가      
        updownStr = x['fluc_tp_cd']         #상승하락보합 코드
        diffStr = x['prv_dd_cmpr']          #전일대비상승하락분
        tradingVolumeStr = x['t_dd_tr_vl'].replace(",", "")  #거래량
        openPriceStr = x['opn_pr_7'].replace(",", "")        #시가    
        highPriceStr = x['hg_pr_7'].replace(",", "")         #고가    
        lowPriceStr = x['lw_pr_7'].replace(",", "")          #저가    
        spotPriceStr = x['end_indx'].replace(",", "")        #현물가    
        settlementPriceStr = x['fut_stt_pr'].replace(",", "")#정산가    
        outstandingStr = x['opn_int_ctr_vl'].replace(",", "")#미결제
        if outstandingStr == '' : 
            outstandingStr = '0'
            
        overnightCdStr = 'N'
        if idx != maxlen - 1 :
            if dtStr == result[idx + 1]['work_dt'].replace('/', '') : 
                overnightCdStr = 'Y'
            
        print dtStr, isucdStr, overnightCdStr, closePriceStr, updownStr, diffStr, tradingVolumeStr, openPriceStr, highPriceStr, lowPriceStr, spotPriceStr, settlementPriceStr, outstandingStr 
        
        resultDic = {}
        resultDic['dt'] = dtStr
        resultDic['ticker'] = isucdStr
        resultDic['close_price'] = closePriceStr
        resultDic['open_price'] = openPriceStr
        resultDic['high_price'] = highPriceStr
        resultDic['low_price'] = lowPriceStr
        resultDic['volume'] = tradingVolumeStr
        resultDic['settlement_price']= settlementPriceStr
        resultDic['spot_price'] = spotPriceStr
        resultDic['outstanding_volume'] = outstandingStr
        resultDic['overnight_cd'] = overnightCdStr
        
        p = FuturesData(**resultDic)
        idx += 1
        p.save()
        
        
