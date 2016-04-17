#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 17.

@author: jayjl
'''
from Parser.models import StockInfo, StockData, StockInvestor, StockShort,\
    StockSuspension
import urllib2
import json
from Parser.test.testAnything import tickerLists

class DataExtractor(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def getCode(self, address):
        try : 
            codeR = urllib2.Request(address)
            codeU = urllib2.urlopen(codeR)
        except : 
            codeR = urllib2.Request(address)
            codeU = urllib2.urlopen(codeR)
        finally:
            return codeU.read()
    
    def getTickerLists(self):
        return StockInfo.objects.filter(data_source = 'KRX')
        
    def getStockHistoricalData(self):
        '''
        Extract the historical stock data from the KRX
        testKRXStocks02
        '''
        
        startDateStr = ''
        endDateStr = ''   
        dateGubunStr = '2' #1:실시간, 2:일별, 3:월별
        
        tickerLists = self.getTickerLists()
        
        for ticker in tickerLists : 
            issueCodeStr = ticker.ticker
            
            codeAddressStr = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0402%2F04020100%2Fmkd04020100t3_02&name=chart"            
            codeStr = self.getCode(codeAddressStr)
            
            address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx?' +\
                '&isu_cd=' + issueCodeStr +\
                '&dateGubun=' + dateGubunStr +\
                '&fromdate=' + startDateStr +\
                '&todate=' + endDateStr +\
                '&code=' + codeStr            
            response = self.getCode(address)
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
                
                print issueCodeStr, dtStr, closePriceStr, updownStr, diffStr, volumeStr, amountStr, openPriceStr,highPriceStr,lowPriceStr,marketCapStr, listedShareStr
                
                resultDic = {}
                resultDic['dt'] = dtStr
                resultDic['ticker'] = issueCodeStr
                resultDic['price_close'] = closePriceStr
                resultDic['price_open'] = openPriceStr
                resultDic['price_high'] = highPriceStr
                resultDic['price_low'] = lowPriceStr
                resultDic['volume'] = volumeStr
                resultDic['amount'] = amountStr
                resultDic['marketcap'] = marketCapStr
                resultDic['listed_shares'] = listedShareStr
                
                p, created = StockData.objects.get_or_create(dt = dtStr, 
                                                             ticker = issueCodeStr,
                                                             defaults = resultDic) 
                if not created : 
                    p.save()
    
    def getStockInvestorData(self):
        '''
        Extract the trade information w.r.t. investors from the KRX
        testKRXStocks03
        '''
        
        startDateStr = ''
        endDateStr = ''
        periodSelectorStr = 'day'
        
        codeAddressStr = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1002%2F10020101%2Fmkd10020101&name=form'        
        codeStr = self.getCode(codeAddressStr)
        
        tickerLists = self.getTickerLists()
        
        for ticker in tickerLists : 
            issueCodeStr = ticker.ticker
        
            address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
                '?isu_cd=' + issueCodeStr +\
                '&period_selector=' + periodSelectorStr +\
                '&fromdate=' + startDateStr +\
                '&todate=' + endDateStr +\
                '&code=' + codeStr        
            response = self.getCode(address)
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
                
                print issueCodeStr, codeStr, buyvolumeStr, sellvolumeStr, buyamountStr, sellamountStr
                
                resultDic = {}
                resultDic['dt'] = startDateStr
                resultDic['ticker'] = issueCodeStr
                resultDic['investor_cd'] = codeStr
                resultDic['buy_amount'] = buyamountStr
                resultDic['buy_volume'] = buyvolumeStr
                resultDic['sell_amount'] = sellamountStr
                resultDic['sell_volume'] = sellvolumeStr
                
                p, created = StockInvestor.objects.get_or_create(dt = startDateStr, 
                                                                 ticker = issueCodeStr,
                                                                 investor_cd = codeStr,
                                                                 defaults = resultDic) 
                if not created : 
                    p.save() 
    
    def getStockShortSaleData(self):
        '''
        Extract the short sale data from the KRX
        testKRXStocks04
        '''
        startDateStr = ''
        endDateStr = ''
        jisuSchTypeStr = '1' #1:개별종목, 2:개별지수
        
        tickerLists = self.getTickerLists()        
        for ticker in tickerLists : 
            issueCodeStr = ticker.ticker
            
            codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F10%2F1002%2F10020104%2Fmkd10020104&name=form'
            codeStr = self.getCode(codeAddress)
            
            address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
                '?jisu_sch_type=' + jisuSchTypeStr +\
                '&isu_cd=' + issueCodeStr +\
                '&period_strt_dd=' + startDateStr +\
                '&period_end_dd=' + endDateStr +\
                '&code=' + codeStr
            
            response = self.getCode(address)
            result = json.loads(response)['block1']
            
            for x in result : 
                dtStr = x['trd_dd'].replace('/','')
                shortvolumeStr = int(x['srtsell_vol'].replace(',', '')) 
                shortvalueStr = int(x['srtsell_val'].replace(',', '')) * 1000
                totalvolumeStr = int(x['all_vol'].replace(',', '')) * 1000
                totalvalueStr = int(x['all_val'].replace(',', '')) * 1000000
                totalshareStr = int(x['all_shrs'].replace(',', '')) * 1000
                
                print issueCodeStr, dtStr, shortvolumeStr, shortvalueStr, totalvolumeStr, totalvalueStr, totalshareStr
                
                resultDic = {}
                resultDic['dt'] = dtStr
                resultDic['ticker'] = issueCodeStr
                resultDic['volume'] = shortvolumeStr
                resultDic['amount'] = shortvalueStr
                resultDic['total_volume'] = totalvolumeStr
                resultDic['total_amount'] = totalvalueStr
                resultDic['total_shares'] = totalshareStr
                
                p, created  = StockShort.objects.get_or_create(dt = dtStr,
                                                               ticker = issueCodeStr,
                                                               defaults = resultDic)
                if not created : 
                    p.save()
    
    def getStockNewIssuedLists(self):
        '''
        New Issued Stock Lists from the KRX
        testKRXStocks05
        '''
        
        dataSourceStr = 'KRX'
        countryStr = 'KR'
        ccyCdStr = 'KRW'
        startDateStr = '20150408'
        endDateStr = '20160408'
        marketGubunStr = 'ALL'
        bndlstTypStr = '1' # 1 : 신규상장, 2: 재상장

        codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0406%2F04060401%2Fmkd04060401_01&name=form'
        codeStr = self.getCode(codeAddress)
        
        address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
            '?market_gubun=' + marketGubunStr +\
            '&bnd_lst_typ=' + bndlstTypStr +\
            '&fromdate=' + startDateStr +\
            '&todate=' + endDateStr +\
            '&code=' + codeStr
        
        response = self.getCode(address)
        result = json.loads(response)['block1']
        
        for x in result : 
            isucdStr = x['isu_cd']
    
            searchCodeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=COM%2Ffinder_stkisu&name=form'            
            searchCodeStr = self.getCode(searchCodeAddress)
        
            searchAddress = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
                '?no=P1' +\
                '&mktsel=ALL' +\
                '&searchText=' + isucdStr +\
                '&code=' + searchCodeStr
                        
            searchResponse = self.getCode(searchAddress)
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
            resultDic['data_source'] = dataSourceStr
            
            p = StockInfo(**resultDic)
            p.save() 
    
    def getStockDelistingLists(self):
        '''
        Stock delisting Lists from the KRX
        testKRXStocks06
        '''
        
        startDateStr = ''
        endDateStr = ''
        
        codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0406%2F04060600%2Fmkd04060600&name=form'
        codeStr = self.getCode(codeAddress)
        
        address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' +\
            '?market_gubun=ALL' +\
            '&fromdate=' + startDateStr +\
            '&todate=' + endDateStr +\
            '&code=' + codeStr
    
        response = self.getCode(address)
        result = json.loads(response['block1'])
        
        for x in result : 
            isuCdStr = x['isu_cd']            
            list = StockInfo.objects.filter(short_ticker = isuCdStr)
            
            #TODO
    
    
    def getStockSuspendedLists(self):
        '''
        Suspension Stock lists from the KRX
        testKRXStocks07
        '''
        
        today = ''        
        codeAddress = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?bld=MKD%2F04%2F0403%2F04030300%2Fmkd04030300&name=form'
        codeStr = self.getCode(codeAddress)
        
        address = 'http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx' + \
            '?gubun=ALL' + \
            '&code=' + codeStr        
        response = self.getCode(address)
        result = json.loads(response)['block1']
        
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
    
    
        
        
        