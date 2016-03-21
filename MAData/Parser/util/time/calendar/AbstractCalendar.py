'''
Created on 2015. 8. 15.

@author: jayjl
'''
from abc import ABCMeta, abstractmethod

from Parser.util.time.BusinessDayConvention import BusinessDayConvention


class Calendar():
    __metaclass__ = ABCMeta
    
    def __init__(self):
        '''
        Constructor
        '''
    
    @abstractmethod
    def isBusinessDay(self, date): pass
    
    @abstractmethod
    def isHoliday(self, date): pass
    
    @abstractmethod
    def isWeekend(self, date): pass
    
    @abstractmethod
    def getDayOfWeek(self, date): pass
    
    @abstractmethod
    def adjustDate(self, date, convention): pass
    
    @abstractmethod
    def getBusinessDayFromDate(self, date, number): pass
    
class AbstractCalendar(Calendar):
    
    holidays = []
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def isBusinessDay(self, date):
        return not self.isHoliday(date)
    
    def isWeekend(self, date):
        w = self.getDayOfWeek(date)
        if w is 0 or w is 1 :
            return True
        else :
            return False
    
    def getDayOfWeek(self, date):
        day = self.getDayOfWeekByZellersCongruence(date)
        return day
    
    def getDayOfWeekByZellersCongruence(self, date):
        y = date.getYear()
        m = date.getMonth()
        d = date.getDay()
        if (m == 1) or (m == 2) :
            m = m + 12
            y = y - 1
        
        x = (y + y / 4 - y / 100 + y / 400 + (int) (2.6 * m + 2.6) + d) % 7;
        return x
    
    def adjustDate(self, date, convention):
        d1 = date
        if convention is BusinessDayConvention.FOLLOWING or convention is BusinessDayConvention.MODIFIED_FOLLOWING : 
            while self.isHoliday(d1) :
                d1 = d1.plusDays(1)
            if convention is BusinessDayConvention.MODIFIED_FOLLOWING : 
                if d1.getMonth() != date.getMonth() :
                    return self.adjustDate(date, BusinessDayConvention.PRECEDING)
        elif convention is BusinessDayConvention.PRECEDING or convention is BusinessDayConvention.MODIFIED_PRECEDING :
            while self.isHoliday(d1) :
                d1 = d1.plusDays(-1)
            if convention is BusinessDayConvention.MODIFIED_PRECEDING : 
                if d1.getMonth() != date.getMonth() :
                    return self.adjustDate(date, BusinessDayConvention.FOLLOWING)
        elif convention is BusinessDayConvention.NEAREST : 
            d2 = self.adjustDate(date, BusinessDayConvention.PRECEDING)
            d3 = self.adjustDate(date, BusinessDayConvention.FOLLOWING)
            if d2.getDay(d1) < d1.getDay(d3) : 
                return d2
            else :
                return d3
        
        return d1
    
    def getBusinessDayFromDate(self, date, number):
        tmpLagDate = date
        increment = -1 if number < 0 else 1
        for index in range(0, abs(number)):                    
            tmpLagDate = self.adjustDate(tmpLagDate.plusDays(increment),
                                         BusinessDayConvention.PRECEDING)
        return tmpLagDate
        
class DelegateCalendar(AbstractCalendar):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.delegate = Calendar()
    
    def setDelegate(self, calendar):
        self.delegate = calendar
    
    def isBusinessDay(self, date):
        return self.delegate.isBusinessDay(date)
        
    def isHoliday(self, date):
        return self.delegate.isHoliday(date)
    
    def isWeekend(self, date):
        return self.delegate.isWeekend(date)
    
    def adjustDate(self, date, convention):
        return self.delegate.adjustDate(date, convention)
    
    def getBusinessDayFromDate(self, date, number):
        return self.delegate.getBusinessDayFromDate(date, number)
    