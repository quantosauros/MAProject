'''
Created on 2015. 8. 18.

@author: Jay
'''
from util.time.BusinessDayConvention import BusinessDayConvention


class Period():
    
    def __init__(self, asOfDate, calendar):
        
        self._convention = BusinessDayConvention.FOLLOWING
        self._asOfDate = calendar.adjustDate(asOfDate, BusinessDayConvention.MODIFIED_PRECEDING)        
        self._calendar = calendar
        
    def getPeriodByVertex(self, vertex):
        year = vertex.getYear()
        month = vertex.getMonth()
        day = vertex.getDay()
        #tmpDate = self._asOfDate.plusDays(-5)
        tmpDate = self._asOfDate.plusYears(-year)
        tmpDate = tmpDate.plusMonths(-month)
        tmpDate = tmpDate.plusDays(-day)
        
        period = []
        d1 = self._calendar.adjustDate(tmpDate, 
                        BusinessDayConvention.MODIFIED_PRECEDING)
        period.append(d1)
        
        while not d1.isEqual(self._asOfDate) :
            d1 = self._calendar.adjustDate(d1.plusDays(1), self._convention)
            period.append(d1)        
        
        return period
    
    def getPeriodByNumber(self, number):        
        period = []
        
        tmpLagDate = self._asOfDate
        for index in range(0, number):                    
            tmpLagDate = self._calendar.adjustDate(tmpLagDate.plusDays(-1),
                                                   BusinessDayConvention.PRECEDING)
            period.append(tmpLagDate)       
        period.reverse()
        return period
    
    
    