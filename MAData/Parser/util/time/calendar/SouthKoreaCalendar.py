'''
Created on 2015. 8. 15.

@author: jayjl
'''

from lunardate import LunarDate

from Parser.util.time.calendar.AbstractCalendar import DelegateCalendar, \
    AbstractCalendar


class SouthKoreaCalendar(DelegateCalendar):
    
    def __init__(self, market):
        '''
        Constructor
        '''
        if market is 0 :
            delegate = SouthKoreaSettlementCalendar()
        elif market is 1 : 
            delegate = SouthKoreaKRXCalendar()
        else :
            None
            
        self.setDelegate(delegate)
        
    @staticmethod
    def getCalendar(market):
        if market is 0 :
            return SouthKoreaCalendar(0)
        elif market is 1 : 
            return SouthKoreaCalendar(1)
        else :
            None
        
class SouthKoreaSettlementCalendar(AbstractCalendar):
    
    def isHoliday(self, date):
        y = date.getYear()
        m = date.getMonth()
        d = date.getDay()
        lDay = LunarDate.fromSolarDate(y, m, d)
        lm = lDay.month
        ld = lDay.day
        
        flag = ((m == 1) and (d == 1)) \
            or ((m == 3) and (d == 1)) \
            or (d == 5 and m == 4 and y <= 2005) \
            or(d == 1 and m == 5) \
            or(d == 5 and m == 5) \
            or (d == 6 and m == 6) \
            or (d == 17 and m == 7 and y <= 2007) \
            or(d == 15 and m == 8) \
            or (d == 3 and m == 10) \
            or ((m == 10) and (d == 9) and (y >= 2013)) \
            or ((m == 12) and (d == 25)) \
            or ((lm == 12) and (ld == 31))\
            or ((lm == 1) and (ld == 1))\
            or ((lm == 1) and (ld == 2))\
            or ((lm == 4) and (ld == 8))\
            or ((lm == 8) and (ld == 14))\
            or ((lm == 8) and (ld == 15))\
            or ((lm == 8) and (ld == 16))\
            or (d == 15 and m == 4 and y == 2004)\
            or (d == 31 and m == 5 and y == 2006)\
            or (d == 19 and m == 12 and y == 2007)\
            or (d ==  9 and m == 4 and y == 2008)\
            or (d ==  2 and m == 6 and y == 2010)\
            or (d == 11 and m == 4 and y == 2012)\
            or (d == 19 and m == 12 and y == 2012)\
            or (d ==  4 and m == 6 and y == 2014)\
            or (d == 13 and m == 4 and y == 2016)\
            or (d == 20 and m == 12 and y == 2017)\
            or (d == 18 and m == 2 and y == 2015) \
            or (d == 10 and m == 9 and y == 2014)
        
        if self.isWeekend(date) or flag :
            return True
        else : 
            return False
        
class SouthKoreaKRXCalendar(SouthKoreaSettlementCalendar):
    
    def isHoliday(self, date):
        m = date.getMonth()
        d = date.getDay()
        w = self.getDayOfWeek(date)
        
        if super(SouthKoreaKRXCalendar, self).isHoliday(date) \
            or ((m == 5) and (d == 1))\
            or ((m == 12) and (d == 31))\
            or ((m == 12) and (d == 30) and (w == 6))\
            or ((m == 12) and (d == 29) and (w == 6)) :
            return True
        else :
            return False
        
        
        
        
        
        