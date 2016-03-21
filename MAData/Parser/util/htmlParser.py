'''
Created on 2015. 5. 12.

@author: Jay
'''
from lxml import html

class htmlParser:
            
    def __init__(self, encodingMethod = 'utf-8'):        
        self._parser = html.HTMLParser(encoding = encodingMethod)
        self._html = None
        self._url = None
        
    def setURL(self, url):
        if self._html is None :
            self._html = html.parse(url, parser = self._parser)
            self._url = url
        elif self._url != url :
            self._html = html.parse(url, parser = self._parser)
            self._url = url
        
    def getResult(self, url, xPath):
        self.setURL(url)
        return self._html.xpath(xPath)

    @staticmethod
    def xPathParse(url, xPath, encodingMethod = 'utf-8'):
        parser1 = html.HTMLParser(encoding = encodingMethod)
        htm = html.parse(url, parser = parser1)                
        result = htm.xpath(xPath)
        return result
    
