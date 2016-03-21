'''
Created on 2016. 3. 3.

@author: jayjl
'''
from Parser.util.htmlParser import htmlParser



url = 'http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/bondint/lastrop/BISLastAskPrc.xml&divisionId=MBIS01010010000000&serviceId=&topMenuIndex=0&w2xHome=/xml/&w2xDocumentRoot='

#current price
#xPath = '//*[@class="time_rtq_ticker"]//text()'
pageStr = '1'
#volume
xPath = '//*[@id="grdMain_body_table"]//text()'


result = htmlParser.xPathParse(url, xPath);
#result = htmlParser.xPathParse(url, xPath);

length = len(result)
print length
for idx in range(0, length) :
    print idx, result[idx]
    
