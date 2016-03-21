'''
Created on 2015. 8. 14.

@author: jayjl
'''
import this

class Date():
    '''
    Date Class
    '''
    m_year = 0
    m_month = 0
    m_day = 0
    m_canonicalForm = ""
    m_isEom = False;
    
    TOTAL_DAYS_IN_MONTH = [
        31,
        59,
        90,
        120,
        151,
        181,
        212,
        243,
        273,
        304,
        334,
        365
   ]
    
    LAST_DAY_IN_MONTH = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    ]
    
    def __init__(self, yyyymmdd):
        
        self.m_year = int(yyyymmdd[:4])
        self.m_month = int(yyyymmdd[4:6])
        self.m_day = int(yyyymmdd[6:])
        self.m_canonicalForm = yyyymmdd
    
    def __str__(self):
        return self.m_canonicalForm
    
    def getDt(self):
        return self.m_canonicalForm;
    
    @staticmethod
    def valueOf(yyyymmdd):
        return Date(yyyymmdd)
    
    @staticmethod
    def canonicalForm(year, month, day) :
        yearStr = str(year)
        monthStr = ("0" if month < 10 else "") + str(month)
        dayStr = ("0" if day < 10 else "") + str(day)
        
        return yearStr + monthStr + dayStr
    
    def getDate(self):
        return self.m_canonicalForm
    
    def getYear(self):
        return self.m_year
    
    def getMonth(self):
        return self.m_month
    
    def getDay(self):
        return self.m_day
    
    def getDays(self, date):
        if (self.m_canonicalForm == date.m_canonicalForm) :
            return 0
        
        dayCount2 = date.getDayCountOfYear()
        dayCount = self.getDayCountOfYear()
        
        daycountYear = 0
        if (self.m_year <= date.getYear()) :
            for index in range(self.m_year, date.getYear()) :
                if self.isLeapYear(index) :
                    daycountYear = daycountYear + 366
                else :
                    daycountYear = daycountYear + 365
            
            return daycountYear - dayCount + dayCount2
        else :
            -date.getDays(this) 
        
    
    def getDayCountOfYear(self):
        if (self.m_month == 1) :
            return self.m_day
    
        if self.isLeapYear() & self.m_month > 2 :
            return self.m_day + self.TOTAL_DAYS_IN_MONTH[self.m_month - 2] + 1
        else :
            return self.m_day + self.TOTAL_DAYS_IN_MONTH[self.m_month - 2]
        
    def isLeapYear(self, year = None):
        if year is None :
            year = self.m_year
        if (year & 3) != 0 :
            return False;

        return (year % 100 != 0) or (year % 400 == 0)
    
    def plusYears(self, years):
        if years == 0 :
            return Date(self.m_canonicalForm)

        if self.isLeapYear() and self.m_month == 2 and self.m_day == 29 :
            if self.isLeapYear(self.m_year + years) :
                return Date(Date.canonicalForm(self.m_year + years, self.m_month, self.m_day))
            else :
                return Date(Date.canonicalForm(self.m_year + years, self.m_month, '28'))
            
        else :
            return Date(Date.canonicalForm(self.m_year + years, self.m_month, self.m_day))
    
    def plusMonths(self, months) :
        if months == 0 :
            return Date(Date.canonicalForm(self.m_year, self.m_month, self.m_day))
        
        if months > 0 :
            yearDelta = 0
            newMonth = self.m_month
            newDayOfMonth = self.m_day
            
            if self.m_month + months <= 12 :
                newMonth = self.m_month + months
                newDayOfMonth =  min(newDayOfMonth, self.getLastDayOfMonth(self.m_year + yearDelta, newMonth))
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
            else :
                cnt = 1;
                while self.m_month + months - 12 * cnt > 12 :
                    cnt = cnt + 1
                    
                yearDelta = cnt
                newMonth = self.m_month + months - 12 * cnt
                newDayOfMonth = min(newDayOfMonth, self.getLastDayOfMonth(self.m_year + yearDelta, newMonth))
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
        else :
            yearDelta = 0
            newMonth = self.m_month
            newDayOfMonth = self.m_day

            if self.m_month + months > 0 :
                newMonth = self.m_month + months
                newDayOfMonth = min(newDayOfMonth, self.getLastDayOfMonth(self.m_year + yearDelta, newMonth))
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
            else :
                cnt = 1
                while self.m_month + months + 12 * cnt <= 0 :
                    cnt = cnt + 1
                    
                yearDelta = -cnt
                newMonth = self.m_month + months + 12 * cnt
                newDayOfMonth = min(newDayOfMonth, self.getLastDayOfMonth(self.m_year + yearDelta, newMonth))
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
            
        if self.m_isEom :
            ret2 = Date(ret.m_year, ret.m_month, self.getLastDayOfMonth(ret._year, ret._month));
            ret2.setEom(True);
            return ret2;
        else :
            return ret;
    
    def plusDays(self, days) :
        if days == 0 :
            return Date(Date.canonicalForm(self.m_year, self.m_month, self.m_day))

        if days > 0 :
            yearDelta = 0
            newMonth = self.m_month;
            newDayOfMonth = self.m_day

            dayDelta = self.getLastDayOfMonth().m_day - self.m_day + 1
            
            if (days - dayDelta) < 0 : 
                newDayOfMonth = self.m_day + days;
                return Date(Date.canonicalForm(self.m_year, self.m_month, newDayOfMonth))
            else :
                newMonth = newMonth + 1
                if newMonth > 12 :
                    newMonth = 1
                    yearDelta = yearDelta + 1
                
                newDayOfMonth = 1
                days -= dayDelta
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
                return ret.plusDays(days);
            
        else :
            yearDelta = 0
            newMonth = self.m_month
            newDayOfMonth = self.m_day

            if (self.m_day + days) > 0 :
                newDayOfMonth = self.m_day + days;
                return Date(Date.canonicalForm(self.m_year, self.m_month, newDayOfMonth))
            else :
                newMonth = newMonth - 1
                if newMonth <= 0 :
                    newMonth = 12
                    yearDelta = yearDelta - 1
                
                newDayOfMonth = self.getLastDayOfMonth(self.m_year + yearDelta, newMonth)
                days += days + self.m_day;
                ret = Date(Date.canonicalForm(self.m_year + yearDelta, newMonth, newDayOfMonth))
                return ret.plusDays(days);
            
    def getLastDayOfMonth(self, year = None, month = None) :
        if year is None and month is None : 
            if self.isLeapYear(year) and month == 2 :
                return Date(Date.canonicalForm(self.m_year, self.m_month, self.LAST_DAY_IN_MONTH[self.m_month - 1] + 1))
            else :
                return Date(Date.canonicalForm(self.m_year, self.m_month, self.LAST_DAY_IN_MONTH[self.m_month - 1]))
        else : 
            if self.isLeapYear(year) and month == 2 :
                return self.LAST_DAY_IN_MONTH[month - 1] + 1
            else :
                return self.LAST_DAY_IN_MONTH[month - 1]
    def diff(self, date):
        return -self.getDays(date)
    
    def setEom(self, isEom):
        self.m_isEom = isEom
        
    def getEom(self):
        return self.m_isEom
    
    def isEqual(self, date):
        if self.m_canonicalForm == date.m_canonicalForm :
            return True
        else :
            return False
    