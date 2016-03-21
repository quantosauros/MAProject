'''
Created on 2016. 3. 12.

@author: jayjl
'''
from Parser.util.DataCollector import DataCollector


startDate = "2016-01-01"
endDate = "2016-04-01"

instrumentType = DataCollector.INDEX

DataCollector.getHistoricalData(startDate, endDate, instrumentType)