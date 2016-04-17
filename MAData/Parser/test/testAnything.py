#-*- coding: utf-8 -*-
'''
Created on 2016. 4. 15.

@author: jayjl
'''
from django.db.models import Count
from django.db.models.aggregates import Min

from Parser.util.time.calendar.SouthKoreaCalendar import SouthKoreaCalendar
from Parser.util.time.Date import Date
from Parser.util.time.BusinessDayConvention import BusinessDayConvention
from django.db.models.aggregates import Min
from Parser.models import StockData, StockInvestor


tickerLists = StockData.objects.values('ticker').annotate(numm = Min('dt', distinct=True))

calendar = SouthKoreaCalendar.getCalendar(1)

startDate = calendar.adjustDate(Date.valueOf('20060101'),
                                    BusinessDayConvention.FOLLOWING)

endDate = calendar.adjustDate(Date.valueOf('20061231'),
                              BusinessDayConvention.FOLLOWING)

processDate = startDate

while processDate.diff(endDate) <= 0 :
       
    for tic in tickerLists :
        print processDate.getDt(),tic['ticker'], tic['numm']
         
        firstDt = Date.valueOf(str(tic['numm']))
        print firstDt.getDate()            
        if processDate.diff(firstDt) >= 0 :
            continue
         
        isuCdStr = tic['ticker']    
        
        p = StockInvestor.objects.filter(ticker = str(isuCdStr)).filter(dt = str(processDate.getDt()))
        
        for r in p :
            r.delete()
            
    processDate = calendar.adjustDate(processDate.plusDays(1),
                                      BusinessDayConvention.FOLLOWING)
            