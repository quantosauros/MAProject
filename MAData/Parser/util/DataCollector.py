'''
Created on 2016. 3. 12.

@author: jayjl
'''
import urllib2
import xml.etree.ElementTree as ET
from yahoo_finance import Share
from Parser.models import FxInfo, EtfInfo, StockInfo, IndexInfo, FxData, EtfData, \
    StockData, IndexData, StockDetail, IrData
from Parser.util.time.Date import Date
from Parser.util.time.calendar.AbstractCalendar import Calendar
from Parser.util.time.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from Parser.util.time.BusinessDayConvention import BusinessDayConvention


class DataCollector(object):
    
    STOCK = "STOCK"
    FX = "FX"
    ETF = "ETF"
    INDEX = "INDEX"

    IRMAP = {
           'KTB 1y' : 'KTB_1Y', 
           'KTB 3y' :  'KTB_3Y', 
           'KTB 5y' :  'KTB_5Y',
           'KTB10y' :  'KTB_10Y', 
           'KTB 20y' :  'KTB_20Y', 
           'KTB 30y'  :  'KTB_30Y',
           'NHB1 5y' : 'NHB1_5Y', 
           'MSB 91d' :  'MSB_3M', 
           'MSB 1y' :  'MSB_1Y',
           'MSB 2y' :  'MSB_2Y', 
           'KEPCO 3y' :  'KEPCO_3Y', 
           'KDB 1y' :  'KDB_1Y',
           'Corp 3y-non AA-' : 'CORPNONAAm_3Y', 
           'Corp 3y-non BBB-' :  'CORPNONBBBm_3Y',
           'CD 91d' :  'CD_3M', 
           'CP 91d' :  'CP_3M',
           }

    @staticmethod
    def getHistoricalData(startDate, endDate, instrumentType):
    
        if instrumentType is DataCollector.FX :        
            tickerLists = FxInfo.objects.values('ticker', 'name')
        elif instrumentType is DataCollector.ETF : 
            tickerLists = EtfInfo.objects.values('ticker', 'name')
        elif instrumentType is DataCollector.STOCK : 
            tickerLists = StockInfo.objects.values('ticker', 'name')
        elif instrumentType is DataCollector.INDEX : 
            tickerLists = IndexInfo.objects.values('ticker', 'name')
        
        tickerLen = len(tickerLists)
            
        for tickerIndex in range(0, tickerLen) :
            tickerStr = tickerLists[tickerIndex]['ticker']
            
            yahooApi = Share(tickerStr)
            
            result = yahooApi.get_historical(startDate, endDate)
            
            for dateIndex in range(0, len(result)) :
                dateStr = result[dateIndex]['Date'].replace("-", "")
                openStr = result[dateIndex]['Open']
                closeStr = result[dateIndex]['Close']
                lowStr = result[dateIndex]['Low']
                highStr = result[dateIndex]['High']
                volumeStr = result[dateIndex]['Volume']
                
                if instrumentType is DataCollector.FX :
                    p = FxData(ticker = tickerStr, dt = dateStr, 
                            price_close = closeStr, price_open = openStr,
                            price_high = highStr, price_low = lowStr,
                            volume = volumeStr)
                elif instrumentType is DataCollector.ETF :
                    p = EtfData(ticker = tickerStr, dt = dateStr, 
                            price_close = closeStr, price_open = openStr,
                            price_high = highStr, price_low = lowStr,
                            volume = volumeStr)
                elif instrumentType is DataCollector.STOCK :
                    p = StockData(ticker = tickerStr, dt = dateStr, 
                            price_close = closeStr, price_open = openStr,
                            price_high = highStr, price_low = lowStr,
                            volume = volumeStr)
                elif instrumentType is DataCollector.INDEX :
                    p = IndexData(ticker = tickerStr, dt = dateStr, 
                            price_close = closeStr, price_open = openStr,
                            price_high = highStr, price_low = lowStr,
                            volume = volumeStr)
                
                p.save()
                
                print tickerStr, dateStr, openStr, closeStr, lowStr, highStr, volumeStr
    
    @staticmethod
    def getStockDetailData():
        
        tickerLists = StockInfo.objects.values('ticker', 'name')        
        tickerLen = len(tickerLists)
        
        for tickerIndex in range(0, tickerLen) :
            tickerStr = tickerLists[tickerIndex]['ticker']        
            share = Share(tickerStr)
            
            dateStr = share.get_trade_datetime()[0:11].replace('-','')
            ma_200Str = DataCollector.convert(share.get_200day_moving_avg())
            ma_50Str = DataCollector.convert(share.get_50day_moving_avg())
            book_valueStr = DataCollector.convert(share.get_book_value())
            volume_avgStr = DataCollector.convert(share.get_avg_daily_volume())
            ebitdaStr = DataCollector.convert(share.get_ebitda())
            dividend_yieldStr = DataCollector.convert(share.get_dividend_yield())
            market_capStr = DataCollector.convert(share.get_market_cap())
            year_highStr = DataCollector.convert(share.get_year_high())
            year_lowStr = DataCollector.convert(share.get_year_low())
            
            print tickerStr, dateStr, ma_200Str, ma_50Str, book_valueStr, volume_avgStr, ebitdaStr, dividend_yieldStr, market_capStr, year_highStr, year_lowStr

            p = StockDetail(dt = dateStr, ticker = tickerStr,
                ma_200 = ma_200Str, ma_50 = ma_50Str,
                book_value = book_valueStr,
                volume_avg = volume_avgStr,
                ebitda = ebitdaStr,
                dividend_yield = dividend_yieldStr,
                market_cap = market_capStr,
                year_high = year_highStr,
                year_low = year_lowStr)

            p.save()
            
    @staticmethod
    def getIRData(startDt, endDt):
        calendar = SouthKoreaCalendar.getCalendar(1)
        
        startDate = calendar.adjustDate(Date.valueOf(startDt),
                                        BusinessDayConvention.FOLLOWING)
        endDate = calendar.adjustDate(Date.valueOf(endDt),
                                      BusinessDayConvention.FOLLOWING)
        
        processDate = startDate
        
        while processDate.diff(endDate) <= 0 :
        
            dateStr = processDate.getDt()
            
            xmlParam  = "<message><proframeHeader>\
                <pfmAppName>BIS-KOFIABOND</pfmAppName>\
                <pfmSvcName>BISLastAskPrcROPSrchSO</pfmSvcName>\
                <pfmFnName>listDay</pfmFnName>\
                </proframeHeader>\
                <systemHeader></systemHeader>\
                <BISComDspDatDTO><val1>" +\
                dateStr +\
                "</val1></BISComDspDatDTO>\
                </message>"
            
            htmlStr = 'http://www.kofiabond.or.kr/proframeWeb/XMLSERVICES/'
            
            r = urllib2.Request(htmlStr, data = xmlParam,
                    headers={'Content-Type': 'application/xml'})        
            u = urllib2.urlopen(r)
            response = u.read()
            
            tree = ET.ElementTree(ET.fromstring(response))
            note = tree.getroot()
            
            for pp in note.iter("BISComDspDatDTO") :
                name = pp.find('val1').text
                valueAt1130 = pp.find('val3').text
                valueAt1530 = pp.find('val4').text
                name_eng = pp.find('val9').text
                
                tickerStr = DataCollector.IRMAP[name_eng]
                
                p = IrData(dt = dateStr, ticker = tickerStr, 
                           value1 = valueAt1130, value2 = valueAt1530)
                
                p.save()
                
                print dateStr, tickerStr, name, name_eng, valueAt1130, valueAt1530
        
            processDate = calendar.adjustDate(processDate.plusDays(1),
                                              BusinessDayConvention.FOLLOWING)
        
    @staticmethod
    def convert(val):
        lookup = {'K': 1000, 'M': 1000000, 'B': 1000000000}
        if val is None :
            return 0
        else :        
            unit = val[-1]
            try:
                number = float(val[:-1])
            except ValueError:
                # do something       
                print "error" 
            if unit in lookup:
                return lookup[unit] * number
            return float(val)


    