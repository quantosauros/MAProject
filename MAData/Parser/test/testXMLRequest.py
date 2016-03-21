#-*- coding: utf-8 -*-

import urllib2
import xml.etree.ElementTree as ET
from Parser.models import IrData

dateStr = "20150318"

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

r = urllib2.Request('http://www.kofiabond.or.kr/proframeWeb/XMLSERVICES/',
                data = xmlParam,
                headers={'Content-Type': 'application/xml'})

u = urllib2.urlopen(r)
response = u.read()

tree = ET.ElementTree(ET.fromstring(response))
note = tree.getroot()

tickers = {
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

for pp in note.iter("BISComDspDatDTO") :
    name = pp.find('val1').text
    valueAt1130 = pp.find('val3').text
    valueAt1530 = pp.find('val4').text
    name_eng = pp.find('val9').text
    
    tickerStr = tickers[name_eng]
    
    p = IrData(dt = dateStr, ticker = tickerStr, 
               value1 = valueAt1130, value2 = valueAt1530)
    
    p.save()
    
    print tickerStr, name, name_eng, valueAt1130, valueAt1530
    
    