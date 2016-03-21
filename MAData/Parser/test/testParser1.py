'''
Created on 2016. 3. 3.

@author: jayjl
'''
from Parser.models import XpathData, XpathInfo, EtfInfo, EtfData
from Parser.util.htmlParser import htmlParser

def convert(val):
    lookup = {'K': 1000, 'M': 1000000, 'B': 1000000000}
    unit = val[-1]
    try:
        number = float(val[:-1])
    except ValueError:
        # do something       
        print "error" 
    if unit in lookup:
        return lookup[unit] * number
    return float(val)


htmlParser = htmlParser()
codeStr = 'YAHOO001'

infoResult = XpathInfo.objects.filter(code = codeStr).values('url')
dataResult = XpathData.objects.filter(xpath_code = codeStr).filter(use = 'Y').values('xpath', 'xpath_index', 'insert_column', 'description')

etfResult = EtfInfo.objects.values('ticker', 'name')

for etfIdx in range(0, len(etfResult)) :
    tickerStr = etfResult[etfIdx]['ticker']
    print etfResult[etfIdx]['name'], tickerStr
    
    for siteIdx in range(0, len(infoResult)) :
        url = infoResult[siteIdx]['url']
        
        resultDic = {}
        resultDic['dt'] = '20160304'
        resultDic['ticker'] = tickerStr
        
        for dataIdx in range(0, len(dataResult)) :
            xPathStr = dataResult[dataIdx]['xpath']
            xPathIndex = dataResult[dataIdx]['xpath_index']
            columnName = str(dataResult[dataIdx]['insert_column'].encode('utf-8'))
            #result = htmlParser.xPathParse(url + ticker, xPathStr)
            result = htmlParser.getResult(url + tickerStr, xPathStr)
            resultStr = result[xPathIndex].replace(',','')
            
            resultStr = convert(resultStr)
                
            resultDic[columnName] = resultStr
            print columnName, result[xPathIndex], resultStr
        
        p = EtfData(**resultDic)
        p.save()
#         etfData, created = EtfData.objects.get_or_create(**resultDic)
#         
#         if created : 
#             etfData.save()
#         else :
#             etfData.update()
